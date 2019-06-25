---
title: cellSecretion (2.0.0)

aliases:
- /language/reference/current/cellSecretion


categories:

- tranformation

---
<!-- COMPUTER GENERATED PAGE!!! DO NOT EDIT DIRECTLY  -->
<!--    must be changed in scripts/templates.py which is processed by scripts/update_refs.py -->

Long form: cellSecretion

Short form: sec

For the abundance term A, `cellSecretion(<abundance>)` or `sec(<abundance>)` denotes the frequency or number of events in which members of `<abundance>` move from cells to regions outside of the cells.


The intent of the `cellSecretion()` function is to provide a simple, standard means of expressing a commonly represented translocation.




### Function Signatures

##### cellSecretion(p|complex|a())

1. One of following function(s): proteinAbundance, complexAbundance, abundance



### Examples


    sec(p(HGNC:RETN))


<pre>cellSecretion(<abundance>)</pre> can be equivalently expressed as

    tloc(p(HGNC:RETN), fromLoc(GO:intracellular), toLoc(GO:"extracellular space"))



---
##### [Request an Edit](https://github.com/belbio/bel_lang_ws/issues/new?title=Doc edit request - cellSecretion (2.0.0))