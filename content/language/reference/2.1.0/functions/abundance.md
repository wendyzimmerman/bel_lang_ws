---
title: abundance (2.1.0)


categories:

- abundance

---
<!-- COMPUTER GENERATED PAGE!!! DO NOT EDIT DIRECTLY  -->
<!--    must be changed in scripts/templates.py which is processed by scripts/update_refs.py -->

Long form: abundance

Short form: a

abundance(ns:v) or a(ns:v) denotes the abundance of the entity designated by the value v in the namespace ns. abundance is a general abundance term that can be used for chemicals or other molecules not defined by a more specific abundance function. Gene, RNA, protein, and microRNA abundances should be represented using the appropriate specific abundance function.




### Function Signatures

##### abundance(NSArg, loc()?)

1. Namespace argument of following type(s): Abundance

1. Zero or one of each function(s): location



### Examples


    a(CHEBI:"oxygen atom")


    a(CHEBI:thapsigargin)



---
##### [Request an Edit](https://github.com/belbio/bel_lang_ws/issues/new?title=Doc edit request - abundance (2.1.0))