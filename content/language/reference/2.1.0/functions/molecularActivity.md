---
title: molecularActivity (2.1.0)


categories:

- process_modifier

---
<!-- COMPUTER GENERATED PAGE!!! DO NOT EDIT DIRECTLY  -->
<!--    must be changed in scripts/templates.py which is processed by scripts/update_refs.py -->

Long form: molecularActivity

Short form: ma

`molecularActivity(ns:v)` or `ma(ns:v)` is used to denote a specific type of activity function within an `activity()` term.

NOTE - The default BEL namespace (DEFAULT) includes commonly used molecular activity types, mapping directly to the BEL 1.0 activity functions.




### Function Signatures

##### molecularActivity(StrArgNSArg)

1. Namespace argument or default namespace argument (without prefix) of following type(s): Activity



### Examples


default BEL namespace, transcriptional activity (DEFAULT namespace is optional)

    act(p(HGNC:FOXO1), ma(DEFAULT:tscript))


GO molecular function namespace, transcriptional activity

    act(p(HGNC:FOXO1), ma(GO:"nucleic acid binding transcription factor activity"))


default BEL namespace, kinase activity

    act(p(HGNC:AKT1), ma(kin))


GO molecular function namespace, kinase activity

    act(p(HGNC:AKT1), ma(GO:"kinase activity"))



---
##### [Request an Edit](https://github.com/belbio/bel_lang_ws/issues/new?title=Doc edit request - molecularActivity (2.1.0))