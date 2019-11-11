#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Usage:  program.py <customer>

Notes:
* ref_{version}.yaml are processed and must be matched with a bel_v{}_expanded.json file
** the expanded json file is created from the bel_v{version}.yaml specification file
* this script creates the version specific function, relation, cheatsheet pages
* this script creates an alias for the current version (called current :)
* all pages that are generated from this script will be tagged with a comment indicating they are not to be edited as edits will be overwritten

"""

import copy
import glob
import json
import os
import re
import shutil

import boto3
import click
import yaml

from templates import (
    cheatsheet_template,
    function_section_template,
    function_template,
    reference_section_template,
    relation_section_template,
    relation_template,
    version_section_template,
)

s3_bucket_name = "resources.bel.bio"
base_issue_url = "https://github.com/belbio/bel_lang_ws/issues/new"
base_pr_url = "https://github.com/belbio/bel_lang_ws/edit/master/content"
script_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ref_dir = f"{base_dir}/content/language/reference"


# TODO - add summary, e.g. to relations/functions front-matter
# ---
# title: abundance (2.0.0)
# summary: abundance for non-specific compounds


def collect_specs(localdev):

    specs = {"bel": {}, "ref": {}}

    if not localdev:
        s3 = boto3.resource("s3")
        bucket = s3.Bucket(name=s3_bucket_name)
        objects = bucket.objects.filter(Prefix="specifications/")
        # objects = bucket.objects.all()
        for obj in objects:
            # print(dir(obj))
            # print(obj)
            basename = os.path.basename(obj.key)
            print(f"Collecting {bucket.name}::{obj.key}  -- {basename}")

            if basename.startswith("bel") and basename.endswith("expanded.json"):
                r = json.loads(obj.get()["Body"].read().decode("utf-8"))
                specs["bel"][r["version"]] = copy.deepcopy(r)
            if basename.startswith("ref"):
                r = yaml.load(obj.get()["Body"].read().decode("utf-8"), Loader=yaml.SafeLoader)
                specs["ref"][r["version"]] = copy.deepcopy(r)

    else:  # Use local versions of BEL Specification files
        files = glob.glob(f"{script_dir}/localdev/*")
        for fn in files:
            basename = os.path.basename(fn)
            print(f"Collecting local file: {fn}")

            if basename.startswith("bel") and basename.endswith("expanded.json"):
                with open(fn, "r") as f:
                    r = json.load(f)
                    specs["bel"][r["version"]] = copy.deepcopy(r)
            if basename.startswith("ref"):
                with open(fn, "r") as f:
                    r = yaml.load(f, Loader=yaml.SafeLoader)
                    specs["ref"][r["version"]] = copy.deepcopy(r)

    # print("DumpVar:\n", json.dumps(specs, indent=4))
    versions = sorted([version for version in specs["bel"] if not re.search("[^\d\.]", version)])
    print("Versions", versions)
    specs["current_version"] = versions[-1]
    weights = {}
    weight = 5
    for version in versions[::-1]:
        weight += 5
        if specs["current_version"] == version:
            weights[version] = 5
        else:
            weights[version] = weight

    specs["version_weights"] = weights
    return specs


def collect_signatures(specs):
    signatures = {}
    for version in specs["bel"]:
        signatures[version] = {}
        for function_key in sorted(specs["ref"][version]["function_section"]["functions"]):
            signatures[version][function_key] = []
            for signature in specs["bel"][version]["functions"]["signatures"][function_key][
                "signatures"
            ]:
                signatures[version][function_key].append(
                    {
                        "summary": signature["argument_summary"],
                        "arguments": signature["argument_help_listing"],
                    }
                )

    return signatures


def create_ref_pages(specs):

    # Remove all dynamically created pages
    if ref_dir.endswith("reference"):
        try:
            shutil.rmtree(ref_dir)
        except Exception:
            pass

    signatures = collect_signatures(specs)
    weights = specs["version_weights"]

    # Create reference pages
    for version in specs["ref"]:
        cheatsheet = {"functions": [], "relations": [], "current": False}
        if specs["current_version"] == version:
            template_version = f"{version} (current)"
        else:
            template_version = version

        # process functions
        for function_key in sorted(specs["ref"][version]["function_section"]["functions"]):
            function = specs["ref"][version]["function_section"]["functions"][function_key]
            function["name"] = function_key
            function["abbreviation"] = specs["bel"][version]["functions"]["info"][function_key][
                "abbreviation"
            ]
            function["signatures"] = signatures[version][function_key]
            function["summary"] = specs["ref"][version]["function_section"]["functions"][
                function_key
            ]["summary"]
            if version == specs["current_version"]:
                function["current"] = True
                cheatsheet["current"] = True
            else:
                function["current"] = False

            issue_url = f"{base_issue_url}?title=Doc edit request - {function_key} ({version})"
            function_page = function_template.render(
                function=function,
                template_version=template_version,
                version=version,
                issue_url=issue_url,
            )
            filename = f"{ref_dir}/{version}/functions/{function_key}.md"
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            with open(filename, "w") as f:
                # print(f"Writing Function file: {filename}")
                f.write(function_page)

        # process relations
        for relation_key in sorted(specs["ref"][version]["relation_section"]["relations"]):
            relation = specs["ref"][version]["relation_section"]["relations"][relation_key]
            relation["name"] = relation_key
            relation["description"] = relation["description"]

            if relation_key in specs["bel"][version]["relations"]["info"]:
                abbrev = specs["bel"][version]["relations"]["info"][relation_key]["abbreviation"]
            else:
                abbrev = relation_key
            relation["summary"] = specs["ref"][version]["relation_section"]["relations"][
                relation_key
            ]["summary"]

            relation["abbreviation"] = abbrev

            if version == specs["current_version"]:
                relation["current"] = True
            else:
                relation["current"] = False

            cheatsheet["relations"].append(
                {"name": relation_key, "abbreviation": abbrev, "summary": relation["summary"]}
            )

            filename = f"{ref_dir}/{version}/relations/{relation_key}.md"
            issue_url = f"{base_issue_url}?title=Doc edit request - {relation_key} ({version})"
            relation_page = relation_template.render(
                relation=relation,
                version=version,
                template_version=template_version,
                issue_url=issue_url,
            )
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            with open(filename, "w") as f:
                # print(f"Writing Relation file: {filename}")
                f.write(relation_page)

        # process cheatsheet
        for function_key in signatures[version]:
            cheatsheet["functions"].append(
                {
                    "name": function_key,
                    "signatures": signatures[version][function_key],
                    "abbreviation": specs["bel"][version]["functions"]["info"][function_key][
                        "abbreviation"
                    ],
                    "summary": specs["bel"][version]["functions"]["info"][function_key][
                        "description"
                    ],
                }
            )

        cheatsheet_page = cheatsheet_template.render(
            cheatsheet=cheatsheet,
            version=version,
            template_version=template_version,
            issue_url=issue_url,
        )
        issue_url = f"{base_issue_url}?title=Doc edit request - Cheatsheet ({version})"
        filename = f"{ref_dir}/{version}/cheatsheet.md"
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w") as f:
            # print(f"Writing Cheatsheet file: {filename}")
            f.write(cheatsheet_page)

        function_section_page = function_section_template.render(
            version=template_version, issue_url=issue_url
        )
        with open(f"{ref_dir}/{version}/functions/_index.md", "w") as f:
            f.write(function_section_page)

        relation_section_page = relation_section_template.render(
            version=version, issue_url=issue_url
        )
        with open(f"{ref_dir}/{version}/relations/_index.md", "w") as f:
            f.write(relation_section_page)

        # Create version section _index.md page
        version_page = version_section_template.render(
            version=version,
            weight=weights[version],
            template_version=template_version,
            issue_url=issue_url,
            changes=specs["ref"][version]["changes"],
        )

        with open(f"{ref_dir}/{version}/_index.md", "w") as f:
            f.write(version_page)

    # Create version section _index.md page
    reference_page = reference_section_template.render(issue_url=issue_url)
    with open(f"{ref_dir}/_index.md", "w") as f:
        f.write(reference_page)


@click.command()
@click.option(
    "--localdev",
    "-l",
    default=False,
    is_flag=True,
    help="Use local version of BEL Specification files (expanded and ref) in ./localdev directory (relative to this script).",
)
def main(localdev):
    specs = collect_specs(localdev)
    create_ref_pages(specs)


if __name__ == "__main__":
    main()
