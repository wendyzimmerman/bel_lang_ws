---
title: hasMembers (2.0.0)

aliases:
- /language/reference/current/hasMembers


categories:

- computed

---
<!-- COMPUTER GENERATED PAGE!!! DO NOT EDIT DIRECTLY  -->
<!--    must be changed in scripts/templates.py which is processed by scripts/update_refs.py -->

Long form: hasMembers
Short form: hasMembers

The `hasMembers` relationship is a special form which enables the assignment of multiple member classes in a single statement where the object of the statement is a set of abundance terms. A statement using `hasMembers` is exactly equivalent to multiple `hasMember` statements. A term may not appear in both the subject and object of the same `hasMembers` statement.

For the abundance terms A, B, C and D, `A hasMembers list(B, C, D)` indicates that A is defined by its member abundance classes B, C and D.


---
##### [Request an Edit](https://github.com/belbio/bel_lang_ws/issues/new?title=Doc edit request - hasMembers (2.0.0))