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

import boto3
import jinja2
import markdown
import requests
import yaml
import json
import copy
import re
import os
from templates import function_template, relation_template, cheatsheet_template

s3_bucket_name = "resources.bel.bio"

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ref_dir = f"{base_dir}/content/language/reference"


def collect_specs():

    specs = {"bel": {}, "belref": {}}

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

    versions = [version for version in specs["bel"] if not re.search("[^\d\.]", version)]
    specs["current_version"] = versions[-1]

    return specs


def create_ref_pages(specs):

    # Create reference pages
    for version in specs["belref"]:
        cheatsheet = {"functions": [], "relations": []}
        # process functions
        for function_key in sorted(specs["belref"][version]["function_section"]["functions"]):
            function = specs["belref"][version]["function_section"]["functions"][function_key]
            function["name"] = function_key
            if version == specs["current_version"]:
                function["current"] = True
            else:
                function["current"] = False

            function["argument_summary"] = [
                sig["argument_summary"]
                for sig in specs["bel"][version]["functions"]["signatures"][function_key][
                    "signatures"
                ]
            ]
            function["argument_help_listing"] = [
                sig["argument_help_listing"]
                for sig in specs["bel"][version]["functions"]["signatures"][function_key][
                    "signatures"
                ]
            ]

            cheatsheet["functions"].append(
                {
                    "name": function_key,
                    "argument_summary": function["argument_summary"],
                    "argument_help_listing": function["argument_help_listing"],
                    "abbreviation": specs["bel"][version]["functions"]["info"][function_key][
                        "abbreviation"
                    ],
                    "summary": specs["bel"][version]["functions"]["info"][function_key][
                        "description"
                    ],
                }
            )

            function_page = function_template.render(function=function, version=version)
            filename = f"{ref_dir}/{version}/functions/{function_key}.md"
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            with open(filename, "w") as f:
                f.write(function_page)

        # process relations
        for relation_key in sorted(specs["belref"][version]["relation_section"]["relations"]):
            relation = specs["belref"][version]["relation_section"]["relations"][relation_key]
            relation["name"] = relation_key

            cheatsheet["relations"].append(
                {
                    "name": relation_key,
                    "abbreviation": specs["bel"][version]["relations"]["info"][relation_key][
                        "abbreviation"
                    ],
                }
            )

            filename = f"{ref_dir}/{version}/relations/{relation_key}.md"
            relation_page = relation_template.render(relation=relation, version=version)
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            with open(filename, "w") as f:
                f.write(relation_page)

        # process cheatsheet
        cheatsheet_page = cheatsheet_template.render(cheatsheet=cheatsheet, version=version)
        filename = f"{ref_dir}/{version}/cheatsheet.md"
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w") as f:
            f.write(cheatsheet_page)


def main():
    specs = collect_specs()
    create_ref_pages(specs)


if __name__ == "__main__":
    main()
