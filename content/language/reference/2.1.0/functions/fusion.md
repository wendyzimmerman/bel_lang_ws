---
title: fusion (2.1.0)


categories:

- other

---
<!-- COMPUTER GENERATED PAGE!!! DO NOT EDIT DIRECTLY  -->
<!--    must be changed in scripts/templates.py which is processed by scripts/update_refs.py -->

Long form: fusion

Short form: fus

`fusion()` or `fus()` expressions can be used in place of a namespace value within a gene, RNA, or protein abundance function to represent a hybrid gene, or gene product formed from two previously separate genes. `fusion()` expressions take the general form:

    fus(ns5':v5', "range5'", ns3':v3', "range3'")

where `ns5':v5'` is a namespace and value for the 5' fusion partner, `range5'` is the sequence coordinates of the 5' partner, `ns3':v3'` is a namespace and value for the 3' partner, and `range3'` is the sequence coordinates for the 3' partner.  Ranges need to be in quotes.




### Function Signatures

##### fusion(NSArg, StrArg, NSArg, StrArg)

1. Namespace argument of following type(s): Gene, RNA, Micro_RNA, Protein

1. String argument of following type(s): /\S+/

1. Namespace argument of following type(s): Gene, RNA, Micro_RNA, Protein

1. String argument of following type(s): /\S+/



### Examples


## RNA abundance of fusion with known breakpoints

The __r.__ designation in the range fields indicates that the numbering uses the RNA sequence as the reference. RNA sequence numbering starts at the transcription initiation site.  You use __c.___ for g() fusions and __p.___ for p() fusions.  These __r.__, __c.__, and __p.__ designations come from http://www.hgvs.org[HGVS variation description] convention.


    r(fus(HGNC:TMPRSS2, "r.1_79", HGNC:ERG, "r.312_5034"))


RNA abundance of fusion with unspecified breakpoints

    r(fus(HGNC:TMPRSS2, "?", HGNC:ERG, "?"))



---
##### [Request an Edit](https://github.com/belbio/bel_lang_ws/issues/new?title=Doc edit request - fusion (2.1.0))