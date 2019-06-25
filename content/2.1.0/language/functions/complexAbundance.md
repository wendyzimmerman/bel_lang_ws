---
title: complexAbundance (2.1.0)


categories:

- abundance

---
<!-- COMPUTER GENERATED PAGE!!! DO NOT EDIT DIRECTLY  -->
<!--    must be changed in scripts/templates.py which is processed by scripts/update_refs.py -->

Long form: complexAbundance

Short form: complex

The complexAbundance() or complex() function can be used with either a namespace value or with a list of abundance terms.

complexAbundance(ns:v) or complex(ns:v) denotes the abundance of the molecular complex designated by the value v in the namespace ns. This form is generally used to identify abundances of named complexes.

complexAbundance(<abundance term list>) denotes the abundance of the molecular complex of members of the abundances denoted by <abundance term list>, a list of abundance terms supplied as arguments. The list is unordered, thus different orderings of the arguments should be interpreted as the same term. Members of a molecular complex retain their individual identities. The complexAbundance() function does not specify the duration or stability of the interaction of the members of the complex.




### Function Signatures

##### complexAbundance(a|p|g|m|r|pop()*, NSArg*, loc()?)

1. Zero or more of each function(s): abundance, proteinAbundance, geneAbundance, microRNAAbundance, rnaAbundance, populationAbundance

1. Zero or more namespace arguments of following type(s): Complex

1. Zero or one of each function(s): location



### Examples


Named complex

    complex(SCOMP:"AP-1 Complex")


complex built from list of abundance terms

    complex(p(HGNC:FOS), p(HGNC:JUN))



---
##### [Request an Edit](https://github.com/belbio/bel_lang_ws/issues/new?title=Doc edit request - complexAbundance (2.1.0))