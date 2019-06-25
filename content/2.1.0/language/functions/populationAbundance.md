---
title: populationAbundance (2.1.0)


categories:

- abundance

---
<!-- COMPUTER GENERATED PAGE!!! DO NOT EDIT DIRECTLY  -->
<!--    must be changed in scripts/templates.py which is processed by scripts/update_refs.py -->

Long form: populationAbundance

Short form: pop

A populationAbundance function captures population changes in a taxon, e.g., a species, subspecies, or phylum, OR a cell population, e.g. adipocytes, epithelial, muscle cells.




### Function Signatures

##### populationAbundance(NSArg, loc()?)

1. Namespace argument of following type(s): Species, Cell

1. Zero or one of each function(s): location



### Examples


Penicillin decreases the population of Streptococcus entericus

    a(CHEBI:penicillin) decreases pop(TAX:1123302)


California Mule Deer increases population of gray wolves

    pop(TAX:598490) increases pop(TAX:9612)


Firmicutes bacteria increases obesity

    pop(TAX:1239) increases path(MESH:Obesity)


A heterogeneous population of microbiome bacteria

    composite(pop(TAX:xxxx), pop(TAX:yyyy)) increases ...


A drug decreases the population of adipocytes

    a(CHEBI:metformin) decreases pop(MESH:"Adipocytes, White")


P. falciparum invasion of RBCs increases malaria

    complex(pop(NCBI:txid5833), pop(CL:erythrocyte)) increases path(DO:malaria)


S. typhimurium in complex with L-ficolin (an opsonin) enhances phagocytosis [PMID:8576206]

    complex(pop(NCBI:txid90371), p(HGNC:FCN2)) increases bp(GO:phagocytosis)



---
##### [Request an Edit](https://github.com/belbio/bel_lang_ws/issues/new?title=Doc edit request - populationAbundance (2.1.0))