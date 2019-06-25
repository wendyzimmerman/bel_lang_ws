---
title: translocation (2.0.0)

aliases:
- /language/reference/current/translocation


categories:

- tranformation

---
<!-- COMPUTER GENERATED PAGE!!! DO NOT EDIT DIRECTLY  -->
<!--    must be changed in scripts/templates.py which is processed by scripts/update_refs.py -->

Long form: translocation

Short form: tloc

For the abundance term A, `translocation(<abundance>, fromLocation(ns1:v1), toLocation(ns2:v2))` or `tloc(<abundance>, fromLoc(ns1:v1), toLoc(ns2:v2))` denotes the frequency or number of events in which members of `<abundance>` move from the location designated by the value +v1+ in the namespace +ns1+ to the location designated by the value `v2` in the namespace `ns2`. Translocation is applied to represent events on the cellular scale, like endocytosis and movement of transcription factors from the cytoplasm to the nucleus.  Special case translocations are handled by the BEL functions: `cellSecretion()`, `cellSurfaceExpression()`.




### Function Signatures

##### translocation(g|p|r|m|complex|a(), fromLoc(), toLoc())

1. One of following function(s): geneAbundance, proteinAbundance, rnaAbundance, microRNAAbundance, complexAbundance, abundance

1. One of following function(s): fromLoc

1. One of following function(s): toLoc



### Examples


endocytosis (translocation from the cell surface to the endosome) of the epidermal growth factor receptor (EGFR) protein can be represented as

    tloc(p(HGNC:EGFR), fromLoc(GO:"cell surface"), toLoc(GO:endosome))



---
##### [Request an Edit](https://github.com/belbio/bel_lang_ws/issues/new?title=Doc edit request - translocation (2.0.0))