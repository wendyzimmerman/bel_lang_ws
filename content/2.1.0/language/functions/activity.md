---
title: activity (2.1.0)


categories:

- process

---
<!-- COMPUTER GENERATED PAGE!!! DO NOT EDIT DIRECTLY  -->
<!--    must be changed in scripts/templates.py which is processed by scripts/update_refs.py -->

Long form: activity

Short form: act

`activity(<abundance>)` or `act(<abundance)` is used to specify events resulting from the molecular activity of an abundance. The `activity()` function provides distinct terms that enable differentiation of the increase or decrease of the molecular activity of a protein from changes in the abundance of the protein. `activity()` can be applied to a protein, complex, or RNA abundance term, and modified with a http://wiki.openbel.org/display/BLVD/Process+Modifier+Function#ProcessModifierFunction-ma()[molecularActivity()] argument to indicate a specific type of molecular activity.




### Function Signatures

##### activity(g|r|m|p|complex(), ma()?)

1. One of following function(s): geneAbundance, rnaAbundance, microRNAAbundance, proteinAbundance, complexAbundance

1. Zero or one of each function(s): molecularActivity



### Examples


    act(p(HGNC:AKT1))



---
##### [Request an Edit](https://github.com/belbio/bel_lang_ws/issues/new?title=Doc edit request - activity (2.1.0))