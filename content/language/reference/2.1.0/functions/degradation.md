---
title: degradation (2.1.0)


categories:

- tranformation

---
<!-- COMPUTER GENERATED PAGE!!! DO NOT EDIT DIRECTLY  -->
<!--    must be changed in scripts/templates.py which is processed by scripts/update_refs.py -->

Long form: degradation

Short form: deg

`degradation(<abundance>)` or `deg(<abundance>)` denotes the frequency or number of events in which a member of `<abundance>` is degraded in some way such that it is no longer a member of `<abundance>`. For example, `degradation()` is used to represent proteasome-mediated proteolysis. The BEL Framework automatically connects +deg(<abundance>)+ to `<abundance>` such that:

    deg(<abundance>) directlyDecreases <abundance>




---
##### [Request an Edit](https://github.com/belbio/bel_lang_ws/issues/new?title=Doc edit request - degradation (2.1.0))