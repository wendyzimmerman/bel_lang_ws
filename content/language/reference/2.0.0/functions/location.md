---
title: location (2.0.0)

aliases:
- /language/reference/current/location


categories:

- abundance_modifier

---
<!-- COMPUTER GENERATED PAGE!!! DO NOT EDIT DIRECTLY  -->
<!--    must be changed in scripts/templates.py which is processed by scripts/update_refs.py -->

Long form: location

Short form: loc

location() or loc() can be used as an argument within any abundance function except compositeAbundance() to represent a distinct subset of the abundance at that location. Location subsets of abundances have the general form:

`f(ns:v, loc(ns:v))`




### Function Signatures

##### location(NSArg)

1. Namespace argument of following type(s): Location



### Examples


Cytoplasmic pool of AKT1 protein

    p(HGNC:AKT1, loc(MESH:Cytoplasm))


Endoplasmic Reticulum pool of Ca2+

    a(CHEBI:"calcium(2+)", loc(GO:"endoplasmic reticulum"))



---
##### [Request an Edit](https://github.com/belbio/bel_lang_ws/issues/new?title=Doc edit request - location (2.0.0))