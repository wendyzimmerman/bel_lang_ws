---
title: cellSurfaceExpression (2.1.0)


categories:

- tranformation

---
<!-- COMPUTER GENERATED PAGE!!! DO NOT EDIT DIRECTLY  -->
<!--    must be changed in scripts/templates.py which is processed by scripts/update_refs.py -->

Long form: cellSurfaceExpression

Short form: surf

`cellSurfaceExpression(<abundance>)` or `surf(<abundance>)` denotes the frequency or abundance of events in which members of `<abundance>` move to the surface of cells. `cellSurfaceExpression(<abundance>)` can be equivalently expressed as:

tloc(<abundance>, fromLoc(GO:intracellular), toLoc(GO:"cell surface"))

The intent of the `cellSurfaceExpression()` function is to provide a simple, standard means of expressing a commonly represented translocation.




### Function Signatures

##### cellSurfaceExpression(p|complex|a())

1. One of following function(s): proteinAbundance, complexAbundance, abundance



### Examples


    surf(p(HGNC:GPER1))



---
##### [Request an Edit](https://github.com/belbio/bel_lang_ws/issues/new?title=Doc edit request - cellSurfaceExpression (2.1.0))