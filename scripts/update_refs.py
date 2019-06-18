#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Usage:  program.py <customer>

Notes:
* belref_{version}.yaml are processed and must be matched with a bel_v{}_expanded.json file
** the expanded json file is created from the bel_v{version}.yaml specification file
* this script creates the version specific function, relation, cheatsheet pages
* this script creates an alias for the current version (called current :)
* all pages that are generated from this script will be tagged with a comment indicating they are not to be edited as edits will be overwritten

"""

import click
import boto3
import jinja2
import markdown
import requests
import glob
import yaml
import json
import copy
import re
import os
from templates import function_template, relation_template, cheatsheet_template

s3_bucket_name = "resources.bel.bio"
base_issue_url = "https://github.com/belbio/bel_lang_ws/issues/new"
base_pr_url = "https://github.com/belbio/bel_lang_ws/edit/master/content"
script_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ref_dir = f"{base_dir}/content/language/reference"


def collect_specs(localdev):

    specs = {"bel": {}, "belref": {}}

    if not localdev:
        s3 = boto3.resource("s3")
        bucket = s3.Bucket(name=s3_bucket_name)
        objects = bucket.objects.filter(Prefix="specifications/")
        # objects = bucket.objects.all()
        for obj in objects:
            # print(dir(obj))
            # print(obj)
            print(f"Collecting {bucket.name}::{obj.key}")

            if "expanded.json" in obj.key:
                r = json.loads(obj.get()["Body"].read().decode("utf-8"))
                specs["bel"][r["version"]] = copy.deepcopy(r)
            if "belref" in obj.key:
                r = yaml.load(obj.get()["Body"].read().decode("utf-8"), Loader=yaml.SafeLoader)

                specs["belref"][r["version"]] = copy.deepcopy(r)

    else:  # Use local versions of BEL Specification files
        files = glob.glob(f"{script_dir}/localdev/*")
        for fn in files:
            print(f"Collecting local file: {fn}")

            if "expanded.json" in fn:
                with open(fn, "r") as f:
                    r = yaml.load(f, Loader=yaml.SafeLoader)
                    specs["bel"][r["version"]] = copy.deepcopy(r)
            if "belref" in fn:
                with open(fn, "r") as f:
                    r = yaml.load(f, Loader=yaml.SafeLoader)
                    specs["belref"][r["version"]] = copy.deepcopy(r)

    versions = [version for version in specs["bel"] if not re.search("[^\d\.]", version)]
    specs["current_version"] = versions[-1]

    return specs


def collect_signatures(specs):
    signatures = {}
    for version in specs["bel"]:
        signatures[version] = {}
        for function_key in sorted(specs["belref"][version]["function_section"]["functions"]):
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

    signatures = collect_signatures(specs)

    # Create reference pages
    for version in specs["belref"]:
        cheatsheet = {"functions": [], "relations": [], "current": False}
        # process functions
        for function_key in sorted(specs["belref"][version]["function_section"]["functions"]):
            function = specs["belref"][version]["function_section"]["functions"][function_key]
            function["name"] = function_key
            function["abbreviation"] = specs["bel"][version]["functions"]["info"][function_key][
                "abbreviation"
            ]
            function["signatures"] = signatures[version][function_key]

            if version == specs["current_version"]:
                function["current"] = True
                cheatsheet["current"] = True
            else:
                function["current"] = False

            issue_url = f"{base_issue_url}?title=Doc edit request - {function_key} ({version})"
            function_page = function_template.render(
                function=function, version=version, issue_url=issue_url
            )
            filename = f"{ref_dir}/{version}/functions/{function_key}.md"
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            with open(filename, "w") as f:
                # print(f"Writing Function file: {filename}")
                f.write(function_page)

        # process relations
        for relation_key in sorted(specs["belref"][version]["relation_section"]["relations"]):
            relation = specs["belref"][version]["relation_section"]["relations"][relation_key]
            relation["name"] = relation_key
            relation["description"] = relation["description"]

            if relation_key in specs["bel"][version]["relations"]["info"]:
                abbrev = specs["bel"][version]["relations"]["info"][relation_key]["abbreviation"]
            else:
                abbrev = relation_key
            relation["abbreviation"] = abbrev

            if version == specs["current_version"]:
                relation["current"] = True
            else:
                relation["current"] = False

            cheatsheet["relations"].append({"name": relation_key, "abbreviation": abbrev})

            filename = f"{ref_dir}/{version}/relations/{relation_key}.md"
            issue_url = f"{base_issue_url}?title=Doc edit request - {relation_key} ({version})"
            relation_page = relation_template.render(
                relation=relation, version=version, issue_url=issue_url
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
            cheatsheet=cheatsheet, version=version, issue_url=issue_url
        )
        issue_url = f"{base_issue_url}?title=Doc edit request - Cheatsheet ({version})"
        filename = f"{ref_dir}/{version}/cheatsheet.md"
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w") as f:
            # print(f"Writing Cheatsheet file: {filename}")
            f.write(cheatsheet_page)


@click.command()
@click.option(
    "--localdev",
    "-l",
    default=False,
    is_flag=True,
    help="Use local version of BEL Specification files (expanded and belref) in ./localdev directory (relative to this script).",
)
def main(localdev):
    specs = collect_specs(localdev)
    create_ref_pages(specs)


if __name__ == "__main__":
    main()
