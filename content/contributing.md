---
title: Contributing
weight: 20
---

We welcome contributions: edits of pages or entirely new pages or sections. We strongly
recommend that you submit an issue before making significant changes to the site to
get feedback and greatly increase the likelihood that the proposed changes are accepted.

You can submit an issue [here](https://github.com/belbio/bel_lang_ws/issues/new).


## Regular pages

Regular pages can be edited directly. The pages are mostly created in markdown and sometimes in html. You can click on the 'Edit this page' link at the bottom of the regular pages and make changes to the page. These edits are submitted to the site managers for review before being incorporated into the website.

<div class="notices note">
<p>You do need to have a <a href="https://github.com">Github account</a> in order to make edits!</p>
</div>


## Auto-generated pages

All of the Language Reference pages (e.g. functions, relations and cheatsheets) are automatically generated from the BEL Language Specification files. You can also tell this type of page as the link at the bottom of the page says 'Request an Edit'.

The simplest approach to editing the automatically generated pages is to submit an issue request so a site manager can make the change for you.

The content for these automatically-generated pages is assembled from the Expanded JSON (bel\_v{*version*}\_expanded.json) file derived from the official BEL Specification YAML (bel_v{*version*}.yaml) file and the BEL Reference (belref_v{*version*}.yaml) file.

#### [BEL Specification files](https://github.com/belbio/bel_specifications/tree/master/specifications)

* BEL Specification YAML file: Official BEL language specification file
* BEL Expanded JSON file: derived file to reformat for easier use by developers
* BEL Reference file: contains additional information for documenting the BEL Language that is not necessary

These pages are created by the script: [update_refs.py](https://github.com/belbio/bel_lang_ws/blob/master/scripts/update_refs.py) using Jinja templates from the [templates.py](https://github.com/belbio/bel_lang_ws/blob/master/scripts/templates.py) file.

---
##### [Edit this page](https://github.com/belbio/bel_lang_ws/edit/master/content/contributing.md)
