
---
title: degradation (2.0.0)


categories:

- tranformation

---
<!-- COMPUTER GENERATED PAGE!!! DO NOT EDIT DIRECTLY  -->
<!--    must be changed in scripts/templates.py which is processed by scripts/update_refs.py -->

## degradation

`degradation(<abundance>)` or `deg(<abundance>)` denotes the frequency or number of events in which a member of `<abundance>` is degraded in some way such that it is no longer a member of `<abundance>`. For example, `degradation()` is used to represent proteasome-mediated proteolysis. The BEL Framework automatically connects +deg(<abundance>)+ to `<abundance>` such that:

    deg(<abundance>) directlyDecreases <abundance>


