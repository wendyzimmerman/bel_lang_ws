---
title: variant (2.1.0)


categories:

- abundance_modifier

---
<!-- COMPUTER GENERATED PAGE!!! DO NOT EDIT DIRECTLY  -->
<!--    must be changed in scripts/templates.py which is processed by scripts/update_refs.py -->

Long form: variant

Short form: var

The `variant("<expression>")` or `var("<expression>")` function can be used as an argument within a `geneAbundance()`, `rnaAbundance()`, `microRNAAbundance()`, or `proteinAbundance()` to indicate a sequence variant of the specified abundance. The `var("")` function takes http://www.hgvs.org/mutnomen/[HGVS] variant description expression, e.g., for a substitution, insertion, or deletion variant. Multiple `var("")` arguments may be applied to an abundance term.




### Function Signatures

##### variant(StrArg)

1. String argument of following type(s): /\S+/



### Examples


reference allele - this is different than `p(HGNC:CFTR)`, the root protein abundance, which includes all variants.

    p(HGNC:CFTR, var("="))


unspecified variant

    p(HGNC:CFTR, var("?"))


CFTR substitution variant Glycine 576 Alanine (HGVS __NP_000483.3:p.Gly576Ala__). Because a specific position is referenced, a namespace value for a non-ambiguous sequence like the http://www.ncbi.nlm.nih.gov/refseq/about/[RefSeq] ID in the lower example is preferred over the HGNC gene symbol. The __p.__ within the `var("")` expression indicates that the numbering is based on a protein sequence.

    p(HGNC:CFTR, var("p.Gly576Ala"))


CFTR substitution variant Glycine 576 Alanine (HGVS __NP_000483.3:p.Gly576Ala__). Because a specific position is referenced, a namespace value for a non-ambiguous sequence like the http://www.ncbi.nlm.nih.gov/refseq/about/[RefSeq] ID in the lower example is preferred over the HGNC gene symbol. The __p.__ within the `var("")` expression indicates that the numbering is based on a protein sequence.

    p(REF:"NP_000483.3", var("p.Gly576Ala"))


CFTR ΔF508 variant (HGVS __NP_000483.3:p.Phe508del__). Because a specific position is referenced, a namespace value for a non-ambiguous sequence like the http://www.ncbi.nlm.nih.gov/refseq/about/[RefSeq] ID in the lower example is preferred over the HGNC gene symbol. The __p.__ within the `var("")` expression indicates that the numbering is based on a protein reference sequence.

    p(HGNC:CFTR, var("p.Phe508del"))


CFTR ΔF508 variant (HGVS __NP_000483.3:p.Phe508del__). Because a specific position is referenced, a namespace value for a non-ambiguous sequence like the http://www.ncbi.nlm.nih.gov/refseq/about/[RefSeq] ID in the lower example is preferred over the HGNC gene symbol. The __p.__ within the `var("")` expression indicates that the numbering is based on a protein reference sequence.

    p(REF:"NP_000483.3", var("p.Phe508del"))


CFTR frameshift variant __(__HGVS__ NP_000483.3:p.Thr1220Lysfs*7). __Because a specific position is referenced, a namespace value for a non-ambiguous sequence like the http://www.ncbi.nlm.nih.gov/refseq/about/[RefSeq] ID in the lower example is preferred over the HGNC gene symbol. The __p.__ within the `var("")` expression indicates that the numbering is based on a protein reference sequence.

    p(HGNC:CFTR, var("p.Thr1220Lysfs"))


CFTR frameshift variant __(__HGVS__ NP_000483.3:p.Thr1220Lysfs*7). __Because a specific position is referenced, a namespace value for a non-ambiguous sequence like the http://www.ncbi.nlm.nih.gov/refseq/about/[RefSeq] ID in the lower example is preferred over the HGNC gene symbol. The __p.__ within the `var("")` expression indicates that the numbering is based on a protein reference sequence.

    p(REF:"NP_000483.3", var("p.Thr1220Lysfs"))


DNA SNP CFTR frameshift at __ΔF508__

    g(SNP:rs113993960, var("delCTT"))


DNA Chromosome CFTR frameshift at __ΔF508__

    g(REF:"NC_000007.13", var("g.117199646_117199648delCTT"))


DNA Because a specific position is referenced, a namespace value for a non-ambiguous sequence like the http://www.ncbi.nlm.nih.gov/refseq/about/[RefSeq] ID in the lower example is preferred over the HGNC gene symbol. The __c.__ within the `var("")` expression indicates that the numbering is based on a coding DNA reference sequence.The coding DNA reference sequence covers the part of the transcript that is translated into protein; numbering starts at the A of the initiating ATG codon, and ends at the last nucleotide of the translation stop codon.

    g(HGNC:CFTR, var("c.1521_1523delCTT"))


DNA Because a specific position is referenced, a namespace value for a non-ambiguous sequence like the http://www.ncbi.nlm.nih.gov/refseq/about/[RefSeq] ID in the lower example is preferred over the HGNC gene symbol. The __c.__ within the `var("")` expression indicates that the numbering is based on a coding DNA reference sequence.The coding DNA reference sequence covers the part of the transcript that is translated into protein; numbering starts at the A of the initiating ATG codon, and ends at the last nucleotide of the translation stop codon.

    g(REF:"NM_000492.3", var("c.1521_1523delCTT"))


Because a specific position is referenced, a namespace value for a non-ambiguous sequence like the http://www.ncbi.nlm.nih.gov/refseq/about/[RefSeq] ID in the lower example is preferred over the HGNC gene symbol. The __c.__ within the `var("")` expression indicates that the numbering is based on a coding DNA reference sequence. The coding DNA reference sequence covers the part of the transcript that is translated into protein; numbering starts at the A of the initiating ATG codon, and ends at the last nucleotide of the translation stop codon.

    r(HGNC:CFTR, var("c.1521_1523delCTT"))


Because a specific position is referenced, a namespace value for a non-ambiguous sequence like the http://www.ncbi.nlm.nih.gov/refseq/about/[RefSeq] ID in the lower example is preferred over the HGNC gene symbol. The __c.__ within the `var("")` expression indicates that the numbering is based on a coding DNA reference sequence. The coding DNA reference sequence covers the part of the transcript that is translated into protein; numbering starts at the A of the initiating ATG codon, and ends at the last nucleotide of the translation stop codon.

    r(REF:"NM_000492.3", var("c.1521_1523delCTT"))


Because a specific position is referenced, a namespace value for a non-ambiguous sequence like the http://www.ncbi.nlm.nih.gov/refseq/about/[RefSeq] ID in the lower example is preferred over the HGNC gene symbol. The __r.__ within the `var("")` expression indicates that the numbering is based on an RNA reference sequence. The RNA reference sequence covers the entire transcript except for the poly A-tail; numbering starts at the transcription initiation site and ends at the transcription termination site.

    r(HGNC:CFTR, var("r.1653_1655delcuu"))


Because a specific position is referenced, a namespace value for a non-ambiguous sequence like the http://www.ncbi.nlm.nih.gov/refseq/about/[RefSeq] ID in the lower example is preferred over the HGNC gene symbol. The __r.__ within the `var("")` expression indicates that the numbering is based on an RNA reference sequence. The RNA reference sequence covers the entire transcript except for the poly A-tail; numbering starts at the transcription initiation site and ends at the transcription termination site.

    r(REF:"NM_000492.3", var("r.1653_1655delcuu"))



---
##### [Request an Edit](https://github.com/belbio/bel_lang_ws/issues/new?title=Doc edit request - variant (2.1.0))