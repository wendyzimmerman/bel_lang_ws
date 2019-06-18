---
title: fragment (2.0.0)

aliases:
- /language/reference/current/fragment


categories:

- abundance_modifier

---
<!-- COMPUTER GENERATED PAGE!!! DO NOT EDIT DIRECTLY  -->
<!--    must be changed in scripts/templates.py which is processed by scripts/update_refs.py -->

Long form: fragment

Short form: frag

The `fragment()` or `frag()` function can be used within a `proteinAbundance()` term to specify a protein fragment, e.g., a product of proteolytic cleavage. Protein fragment expressions take the general form:

`p(ns:v, frag(<range>, <descriptor>))`

where `<range>` (required) is an amino acid range, and `<descriptor>` (optional) is any additional distinguishing information like fragment size or name.

For the examples, HGNC:YFG is 'your favorite gene'. For the first four examples, only the <range> argument is used. The last examples include use of the optional <descriptor>.




### Function Signatures

##### fragment(StrArg, StrArg)

1. String argument of following type(s): /[\d\_\?\*]+/

1. String argument of following type(s): /.*?/



### Examples


fragment with known start/stop

    p(HGNC:YFG, frag("5_20"))


amino-terminal fragment of unknown length

    p(HGNC:YFG, frag("1_?"))


carboxyl-terminal fragment of unknown length

    p(HGNC:YFG, frag("?_*"))


fragment with unknown start/stop

    p(HGNC:YFG, frag("?"))


fragment with unknown start/stop and a descriptor

    p(HGNC:YFG, frag("?", "55kD"))



---
##### [Request an Edit](https://github.com/belbio/bel_lang_ws/issues/new?title=Doc edit request - fragment (2.0.0))