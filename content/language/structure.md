---
title: Structure
date: 2019-04-26T20:30:33-04:00
weight: 10
---


## Language Structure

Knowledge in BEL is expressed as BEL Assertion. Generally, BEL Assertion have the form of a subject - predicate - object triple, where the subject is a BEL Term, the predicate is one of the BEL relationship types (e.g., increases), and the object can be either a BEL Term or a BEL Assertion. A BEL Assertion may also be composed of a subject term only.

BEL Terms are composed of BEL Functions applied to concepts referenced using Namespace identifiers. Each BEL Term represents either an abundance of a biological entity, e.g., human AKT1 protein, or a process such as apoptosis.

BEL Annotations are applied to BEL Assertion to optionally express additional information about the statement itself, such as the citation for the publication reporting the observation, or the context in which the observation was made (e.g., species, tissue, cell line).

## Terms

Two general categories of biological entities are represented as BEL Terms:

* abundances
* processes


### Abundances


Life science experiments often measure the abundance of a type of thing in a given sample or set of samples. BEL Abundance Terms represent classes of abundance, the abundances of specific types of things. Examples include:

* protein abundance of TP53,
* RNA abundance of CCND1
* abundance of the protein AKT1 phosphorylated at serine 21
* abundance of the complex of the proteins CCND1 and CDK4
* abundance of neutrophils

### Processes

BEL Process Terms represent classes of complex phenomena taking place at the level of the cell or the organism, such as the biological process of *cell cycle* or a disease process such as *Cardiomyopathy*. In other cases, BEL Terms may represent classes of specific molecular activities, such as the kinase activity of the AKT1 protein, or a specific chemical reaction like conversion of superoxides to hydrogen peroxide and oxygen.

Measurable biological parameters such as *Blood Pressure* or *Body Temperature* are represented as process BEL Terms. These BEL Terms denote biological activities that, when measured, are reduced to an output parameter.

### BEL Terms as Functional Expressions


BEL Terms are denoted by expressions composed of a BEL Function and a list of arguments. BEL v2.0 specifies a set of approximately 20 functions allowed in term expressions.

The combination of a BEL function and its arguments fully specifies a BEL Term. The BEL Term expression `f(a)` denotes a BEL Term defined by function `f()` applied to an argument `a`. Wherever the same function is applied to the same arguments, the resulting BEL Term references the same biological entity.

The semantics of a BEL Term are determined by the function used in the term expression. For example, the function `proteinAbundance()` is defined such that any term expression using `proteinAbundance()` represents a class of abundance of protein. Many BEL functions take only single values as arguments, providing a structured method of using ontologies and vocabularies in BEL. For example, values in the HUGO Gene Nomenclature Committee (HGNC) vocabulary of official human gene symbols can be used to designate gene, RNA, and protein abundances. The function `proteinAbundance()` could then be applied to an HGNC gene symbol, *AKT1* for example, to indicate the class of protein abundances produced by the AKT1 gene, producing the BEL Term `proteinAbundance(HGNC:AKT1)`.


## Assertions

A BEL Assertion represents an experimental observation, generally reported in a scientific publication, or unpublished experimental data. Generally, BEL Assertions express a causal or correlative relationship between two biological entities. Because BEL Terms are functionally composed, a BEL Assertion can consist of a single BEL Term; this simple statement indicates that the biological entity represented by the term has been observed.

### Example BEL Assertions


####  Subject Term Only


    complex(p(HGNC:CCND1), p(HGNC:CDK4))

The abundance of a complex formed from protein abundances designated by *CCND1* and *CDK4* in the HGNC namespace. This is a subject term only assertion, and indicates that the entity specified by the term has been observed.

#### Causal


    p(HGNC:CCND1) directlyIncreases act(p(HGNC:CDK4))

The abundance of the protein designated by *CCND1* in the HGNC namespace directly increases the activity of the abundance of the protein designated by *CDK4* in the HGNC namespace.

#### Causal


    p(HGNC:BCL2) decreases bp(MESHPP:Apoptosis)

The abundance of the protein designated by *BCL2* in the HGNC namespace decreases the biological process designated by *apoptosis* in the MESHPP (phenomena and processes) namespace.

#### Nested Assertion - Object Term is Assertion


    p(HGNC:GATA1) directlyIncreases (act(p(HGNC:ZBTB16)) directlyIncreases r(HGNC:MPL))

The abundance of the protein designated by *GATA1* in the HGNC namespace directly increases the process in which the activity of the protein abundance designated by *ZBTB16* in the HGNC namespace directly increases the abundance of RNA designated by *MPL* in the HGNC namespace.

---
##### [Edit this page](https://github.com/belbio/bel_lang_ws/edit/master/content/language/structure.md)
