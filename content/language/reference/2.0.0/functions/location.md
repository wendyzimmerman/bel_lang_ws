
---
title: location (2.0.0)


categories:

- abundance_modifier

---
<!-- COMPUTER GENERATED PAGE!!! DO NOT EDIT DIRECTLY  -->
<!--    must be changed in scripts/templates.py which is processed by scripts/update_refs.py -->

## location

location() or loc() can be used as an argument within any abundance function except compositeAbundance() to represent a distinct subset of the abundance at that location. Location subsets of abundances have the general form:

`f(ns:v, loc(ns:v))`



### Examples


Cytoplasmic pool of AKT1 protein

    p(HGNC:AKT1, loc(MESH:Cytoplasm))


Endoplasmic Reticulum pool of Ca2+

    a(CHEBI:"calcium(2+)", loc(GO:"endoplasmic reticulum"))

