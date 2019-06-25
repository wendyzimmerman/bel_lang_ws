---
title: rnaAbundance (2.1.0)


categories:

- abundance

---
<!-- COMPUTER GENERATED PAGE!!! DO NOT EDIT DIRECTLY  -->
<!--    must be changed in scripts/templates.py which is processed by scripts/update_refs.py -->

Long form: rnaAbundance

Short form: r

`rnaAbundance(ns:v)` or `r(ns:v)` denotes the abundance of the RNA designated by the value v in the namespace +ns+, where +v+ references a gene. This function refers to all RNA designated by +ns:v+, regardless of splicing, editing, or polyadenylation stage.




### Function Signatures

##### rnaAbundance(NSArg, loc()?, var()*)

1. Namespace argument of following type(s): RNA

1. Zero or one of each function(s): location

1. Zero or more of each function(s): variant


##### rnaAbundance(fus(), loc()?, var()*)

1. One of following function(s): fusion

1. Zero or one of each function(s): location

1. Zero or more of each function(s): variant



### Examples


    r(HGNC:AKT1)



---
##### [Request an Edit](https://github.com/belbio/bel_lang_ws/issues/new?title=Doc edit request - rnaAbundance (2.1.0))