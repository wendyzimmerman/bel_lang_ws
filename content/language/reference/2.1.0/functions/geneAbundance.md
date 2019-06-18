---
title: geneAbundance (2.1.0)


categories:

- abundance

---
<!-- COMPUTER GENERATED PAGE!!! DO NOT EDIT DIRECTLY  -->
<!--    must be changed in scripts/templates.py which is processed by scripts/update_refs.py -->

Long form: geneAbundance

Short form: g

`geneAbundance(ns:v)` or `g(ns:v)` denotes the abundance of the gene designated by the value v in the namespace ns. `geneAbundance()` terms are used to represent the DNA encoding the specified gene. `geneAbundance()` is considered decreased in the case of a homozygous or heterozygous gene deletion, and increased in the case of a DNA amplification mutation. Events in which a protein binds to the promoter of a gene can be represented using the `geneAbundance()` function.




### Function Signatures

##### geneAbundance(NSArg, loc()?, var()*)

1. Namespace argument of following type(s): Gene

1. Zero or one of each function(s): location

1. Zero or more of each function(s): variant


##### geneAbundance(fus(), loc()?, var()*)

1. One of following function(s): fusion

1. Zero or one of each function(s): location

1. Zero or more of each function(s): variant



### Examples


p53 protein binds the CDKN1A gene

    complex(p(HGNC:TP53), g(HGNC:CDKN1A))



---
##### [Request an Edit](https://github.com/belbio/bel_lang_ws/issues/new?title=Doc edit request - geneAbundance (2.1.0))