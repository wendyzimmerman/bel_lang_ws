
---
title: cellSurfaceExpression (2.0.0)


categories:

- tranformation

---
<!-- COMPUTER GENERATED PAGE!!! DO NOT EDIT DIRECTLY  -->
<!--    must be changed in scripts/templates.py which is processed by scripts/update_refs.py -->

## cellSurfaceExpression

`cellSurfaceExpression(<abundance>)` or `surf(<abundance>)` denotes the frequency or abundance of events in which members of `<abundance>` move to the surface of cells. `cellSurfaceExpression(<abundance>)` can be equivalently expressed as:

tloc(<abundance>, fromLoc(GO:intracellular), toLoc(GO:"cell surface"))

The intent of the `cellSurfaceExpression()` function is to provide a simple, standard means of expressing a commonly represented translocation.



### Examples


    surf(p(HGNC:GPER1))

