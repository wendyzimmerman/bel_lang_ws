---
title: compositeAbundance (2.0.0)

aliases:
- /language/reference/current/compositeAbundance


categories:

- abundance

---
<!-- COMPUTER GENERATED PAGE!!! DO NOT EDIT DIRECTLY  -->
<!--    must be changed in scripts/templates.py which is processed by scripts/update_refs.py -->

Long form: compositeAbundance

Short form: composite

The `compositeAbundance(<abundance term list>)` function takes a list of abundance terms.

The `compositeAbundance()` or `composite()` function is used to represent cases where multiple abundances synergize to produce an effect. The list is unordered, thus different orderings of the arguments should be interpreted as the same term. This function should not be used if any of the abundances alone are reported to cause the effect. `compositeAbundance()` terms should be used only as subjects of statements, not as objects.




### Function Signatures

##### compositeAbundance(a|act|p|g|m|r|complex()*, NSArg*)

1. Zero or more of each function(s): abundance, activity, proteinAbundance, geneAbundance, microRNAAbundance, rnaAbundance, complexAbundance

1. Zero or more namespace arguments of following type(s): Complex



### Examples


IL-6 and IL-23 synergistically induce Th17 differentiation.

    composite(p(HGNC:IL6), complex(GO:"interleukin-23 complex")) increases bp(GO:"T-helper 17 cell differentiation")



---
##### [Request an Edit](https://github.com/belbio/bel_lang_ws/issues/new?title=Doc edit request - compositeAbundance (2.0.0))