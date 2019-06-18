---
title: hasComponents (2.0.0)

aliases:
- /language/reference/current/hasComponents


categories:

- computed

---
<!-- COMPUTER GENERATED PAGE!!! DO NOT EDIT DIRECTLY  -->
<!--    must be changed in scripts/templates.py which is processed by scripts/update_refs.py -->

Long form: hasComponents
Short form: hasComponents

The `hasComponents` relationship is a special form which enables the assignment of multiple complex components in a single statement where the object of the statement is a set of abundance terms. A statement using `hasComponents` is exactly equivalent to multiple `hasComponent` statements. A term may not appear in both the subject and object of the same +hasComponents+ statement.

For the abundance terms A, B, C and D, `A hasComponents list(B, C, D)` indicates that A has components B, C and D.


---
##### [Request an Edit](https://github.com/belbio/bel_lang_ws/issues/new?title=Doc edit request - hasComponents (2.0.0))