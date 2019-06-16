
---
title: complexAbundance (2.0.0)


categories:

- abundance

---
<!-- COMPUTER GENERATED PAGE!!! DO NOT EDIT DIRECTLY  -->
<!--    must be changed in scripts/templates.py which is processed by scripts/update_refs.py -->

## complexAbundance

The complexAbundance() or complex() function can be used with either a namespace value or with a list of abundance terms.

complexAbundance(ns:v) or complex(ns:v) denotes the abundance of the molecular complex designated by the value v in the namespace ns. This form is generally used to identify abundances of named complexes.

complexAbundance(<abundance term list>) denotes the abundance of the molecular complex of members of the abundances denoted by <abundance term list>, a list of abundance terms supplied as arguments. The list is unordered, thus different orderings of the arguments should be interpreted as the same term. Members of a molecular complex retain their individual identities. The complexAbundance() function does not specify the duration or stability of the interaction of the members of the complex.



### Examples


Named complex

    complex(SCOMP:"AP-1 Complex")


complex built from list of abundance terms

    complex(p(HGNC:FOS), p(HGNC:JUN))

