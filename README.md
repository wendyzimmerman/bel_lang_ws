# BEL.bio BEL Language website

![Published](https://github.com/belbio/bel_lang_ws/workflows/Published/badge.svg)

This is the hugo-based website repository for the BEL Language. We are using the
[Learn Hugo theme](https://themes.gohugo.io/hugo-theme-learn/).

## Usage

> Prerequisites: Go, Hugo, aws (Amazon AWS cli and S3 write credentials), pipenv

To start your website run the following commands:

**Development**:

Setup

```
$ git clone git@github.com:belbio/bel_lang_ws.git
$ pipenv install --dev
$ pipenv shell
```

```
$ ./bin/update_refs.py  # Update the generated BEL reference documents (function/relation pages from the BEL Specification files)
$ hugo server -D
```

Or use `make serve`

**Production**:

Any pushes to the `master` branch will be automatically deployed to production
using Github Actions. The .github/workflows/prod.yml file is followed for
publishing the website.

## Directory Structure

We're using the standard directory structure using content pages.

Also note that all of the pages under content/language/reference is created by ./bin/update_refs.py based on content pulled from http://resources.bel.bio/?prefix=specifications/. The ref\*yaml and

```
├─ content/
├ layouts/ # You can add extra layout files here. A sample custom fragment is available as a sample.
├ static/ # Your static files are in this directory.
├ themes/ # Hugo uses this directory as a default to look for themes. Syna theme is a git submodule available in this directory.
├ .gitignore
├ .gitmodules
├ config.toml # Hugo config file containing general settings and menu configs.
```

Further details read our [full documentation](https://learn.netlify.com/en/cont/i18n/).

## Credits

Website:

-   [Hugo](https://gohugo.io/) static site generator
-   [Learn Hugo theme](https://themes.gohugo.io/hugo-theme-learn/)
-   Most of the content was authored by Natalie Catlett, PhD and converted from the OpenBEL AsciiDoc for BEL 2.0
