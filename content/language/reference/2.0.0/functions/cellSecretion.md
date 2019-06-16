
---
title: cellSecretion (2.0.0)


categories:

- tranformation

---
<!-- COMPUTER GENERATED PAGE!!! DO NOT EDIT DIRECTLY  -->
<!--    must be changed in scripts/templates.py which is processed by scripts/update_refs.py -->

## cellSecretion

For the abundance term A, `cellSecretion(<abundance>)` or `sec(<abundance>)` denotes the frequency or number of events in which members of `<abundance>` move from cells to regions outside of the cells.


The intent of the `cellSecretion()` function is to provide a simple, standard means of expressing a commonly represented translocation.



### Examples


    sec(p(HGNC:RETN))


<pre>cellSecretion(<abundance>)</pre> can be equivalently expressed as

    tloc(p(HGNC:RETN), fromLoc(GO:intracellular), toLoc(GO:"extracellular space"))

