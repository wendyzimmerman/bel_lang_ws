---
title: "Namespaces"
date: 2019-04-26T19:15:50-04:00
draft: false
weight: 10
---

BEL is specifically designed to adopt external vocabularies and ontologies, and represent life-science knowledge in the language and schema of the organization collecting or using the knowledge. Thus, BEL Terms are defined by reference to concepts in external vocabularies, which provide a set of well-known domain values, such as the official human gene symbols provided by HGNC (http://www.genenames.org/) . While we consider it good practice to define biological entities with respect to well-defined domains such as public ontologies, no specific vocabulary is essential to the use of BEL, and users are free to define and reference their own vocabularies as needed.

BEL uses Namespaces to unambiguously reference concepts. The user associates a Namespace prefix with an external vocabulary and uses the prefix to refer to elements of the vocabulary. For example, if we associate the Namespace prefix HGNC with the vocabulary of symbols managed by the HGNC committee, we can then compose BEL Terms by referencing the HGNC Namespace prefix and any concept from the HGNC namespace together with a relevant BEL Function, e.g., `proteinAbundance(HGNC:AKT1)` or `rnaAbundance(HGNC:TNF)`.

### Equivalencing between Namespaces

Values from different Namespaces may correspond to the same biological concept. For example, the name AKT1 in the HGNC Namespace refers to the same gene referenced with ID 207 in the EG Namespace (Entrez Gene Identifier) Namespace. The BEL Framework assembles knowledge into a cohesive network, mapping equivalent BEL Terms, e.g., `proteinAbundance(HGNC:AKT1)` and `proteinAbundance(EG:207)`, to a single node in the network. This correspondence of Namespace values is handled in the BEL Framework separately from BEL knowledge representation.

