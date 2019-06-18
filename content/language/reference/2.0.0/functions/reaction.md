---
title: reaction (2.0.0)

aliases:
- /language/reference/current/reaction


categories:

- t

- r

- a

- n

- f

- o

- r

- m

- a

- t

- i

- o

- n

---
<!-- COMPUTER GENERATED PAGE!!! DO NOT EDIT DIRECTLY  -->
<!--    must be changed in scripts/templates.py which is processed by scripts/update_refs.py -->

Long form: reaction

Short form: rxn

`reaction(reactants(<abundance term list1>), products(<abundance term list2>))` denotes the frequency or abundance of events in which members of the abundances in `<abundance term list1>` (the reactants) are transformed into members of the abundances in `<abundance term list2>` (the products).




### Function Signatures

##### reaction(reactants(), products())

1. One of following function(s): reactants

1. One of following function(s): products



### Examples


The reaction in which superoxides are dismutated into oxygen and hydrogen peroxide can be represented as

    rxn(reactants(a(CHEBI:superoxide)), products(a(CHEBI:"hydrogen peroxide"), a(CHEBI:"oxygen")))



---
##### [Request an Edit](https://github.com/belbio/bel_lang_ws/issues/new?title=Doc edit request - reaction (2.0.0))