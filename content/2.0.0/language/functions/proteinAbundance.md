---
title: proteinAbundance (2.0.0)

aliases:
- /language/reference/current/proteinAbundance


categories:

- abundance

---
<!-- COMPUTER GENERATED PAGE!!! DO NOT EDIT DIRECTLY  -->
<!--    must be changed in scripts/templates.py which is processed by scripts/update_refs.py -->

Long form: proteinAbundance

Short form: p

`proteinAbundance(ns:v)` or `p(ns:v)` denotes the abundance of the protein designated by the value +v+ in the namespace +ns+, where +v+ references a gene or a named protein family.




### Function Signatures

##### proteinAbundance(NSArg, loc|frag()?, var|pmod()*)

1. Namespace argument of following type(s): Protein

1. Zero or one of each function(s): location, fragment

1. Zero or more of each function(s): variant, proteinModification


##### proteinAbundance(fus(), loc()?, var()*)

1. One of following function(s): fusion

1. Zero or one of each function(s): location

1. Zero or more of each function(s): variant



### Examples


    p(HGNC:AKT1)


    p(SFAM:"AKT Family")



---
##### [Request an Edit](https://github.com/belbio/bel_lang_ws/issues/new?title=Doc edit request - proteinAbundance (2.0.0))