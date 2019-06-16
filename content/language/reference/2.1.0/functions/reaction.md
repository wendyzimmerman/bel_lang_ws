
---
title: reaction (2.1.0)

aliases:
- /language/reference/current/reaction


categories:

- tranformation

---
<!-- COMPUTER GENERATED PAGE!!! DO NOT EDIT DIRECTLY  -->
<!--    must be changed in scripts/templates.py which is processed by scripts/update_refs.py -->

## reaction

`reaction(reactants(<abundance term list1>), products(<abundance term list2>))` denotes the frequency or abundance of events in which members of the abundances in `<abundance term list1>` (the reactants) are transformed into members of the abundances in `<abundance term list2>` (the products).



### Examples


The reaction in which superoxides are dismutated into oxygen and hydrogen peroxide can be represented as

    rxn(reactants(a(CHEBI:superoxide)), products(a(CHEBI:"hydrogen peroxide"), a(CHEBI:"oxygen")))

