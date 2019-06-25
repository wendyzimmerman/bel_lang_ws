---
title: pathology (2.0.0)

aliases:
- /language/reference/current/pathology


categories:

- process

---
<!-- COMPUTER GENERATED PAGE!!! DO NOT EDIT DIRECTLY  -->
<!--    must be changed in scripts/templates.py which is processed by scripts/update_refs.py -->

Long form: pathology

Short form: path

`pathology(ns:v)` or `path(ns:v)` denotes the disease or pathology process designated by the value +v+ in the namespace +ns+. The +pathology()` function is included to facilitate the distinction of pathologies from other biological processes because of their importance in many potential applications in the life sciences.




### Function Signatures

##### pathology(NSArg)

1. Namespace argument of following type(s): Pathology



### Examples


    pathology(MESH:"Pulmonary Disease, Chronic Obstructive")


    pathology(MESH:adenocarcinoma)



---
##### [Request an Edit](https://github.com/belbio/bel_lang_ws/issues/new?title=Doc edit request - pathology (2.0.0))