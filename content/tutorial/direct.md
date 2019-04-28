---
title: "Direct Relationships"
date: 2019-04-26T20:00:18-04:00
draft: true
---

## Direct Relationships

Direct relationships include direct causal relationships and non-causal relationships that are considered direct because they are self-referential.

## Direct causal relationships

The direct casual relationships included in BEL v2.0 are `directlyIncreases` (`=>`) and `directlyDecreases` (`=|`).

The direct casual relationships are causal relationships where the mechanism of the causal relationship is based on the physical interaction of entities related to the BEL Statement subject and object terms.

If A or B is an <<Abundance Functions, abundance>>, then members of the abundance are part of the interaction. If A or B are <<Xactivity, activities>> activities, then members of the abundances performing the activities physically interact.

===== Examples

====== Abundances and activities

Inhibition of the Patched 1 receptor signaling activity by Hedgehog is represented as direct, because Hedgehog and Patched 1 physically interact:

<span class="assertion">p(PFH:"Hedgehog Family") =| act(p(HGNC:PTCH1))</span>


====== Transcription

In the case of transcriptional activity, if the protein performing the transcriptional activity interacts with the gene that the RNA is transcribed from, the relationship is considered direct. For example, repression of the transcription of miR-21 by FOXO3 protein transcriptional activity is represented as direct because FOXO3 binds the miR-21 promoter:


 act(p(HGNC:FOXO3),ma(tscript)) =| r(HGNC:MIR21)

====== Target term is BEL statement

If B is a BEL Statement, the relationship is considered direct if the subject abundance term for B physically interacts with the abundance term for A. For example, for the BEL Statement:


 p(HGNC:CLSPN) => (act(p(HGNC:ATR), ma(kin)) => p(HGNC:CHEK1, pmod(Ph)))

CLSPN protein is considered to directly activate the phosphorylation of CHEK1 protein by the kinase activity of ATR, because the CLSPN and ATR proteins physically interact.

====== Self-referential relationships

Self-referential causal relationships are generally represented as direct. For example, phosphorylation of GSK3B at serine 9 inhibiting the kinase activity of GSK3B can be represented as:


 p(HGNC:GSK3B, pmod(Ph, S, 9)) =| act(p(HGNC:GSK3B), ma(kin))
