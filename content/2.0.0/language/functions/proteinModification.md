---
title: proteinModification (2.0.0)

aliases:
- /language/reference/current/proteinModification


categories:

- abundance_modifier

---
<!-- COMPUTER GENERATED PAGE!!! DO NOT EDIT DIRECTLY  -->
<!--    must be changed in scripts/templates.py which is processed by scripts/update_refs.py -->

Long form: proteinModification

Short form: pmod

The `proteinModification()` or `pmod()` function can be used only as an argument within a `proteinAbundance()` function to indicate modification of the specified protein. Multiple modifications can be applied to the same protein abundance. Modified protein abundance term expressions have the general form:

 p(ns:protein_value, pmod(ns:type_value, \<code\>, \<pos\>))

`type_value` (required) is a namespace value for the type of modification , **`<code>`** (optional) is a single-letter or three-letter code for one of the twenty standard amino acids, and `<pos>` (optional) is the position at which the modification occurs based on the reference sequence for the protein. If **`<pos>`** is omitted, then the position of the modification is unspecified. If both **`<code>`** and **`<pos>`** are omitted, then the residue and position of the modification are unspecified. NOTE - the default BEL namespace includes commonly used protein modification types.

Additional modification types can be requested as needed, or an external vocabulary can be used. Like other BEL namespace values, these modification types can be equivalenced to values in other vocabularies.

### Protein Modification Default Namespace

| **Label** | **Synonym**|
|-----------|------------|
| Ac | acetylation |
| ADPRib | ADP-ribosylation, ADP-rybosylation, adenosine diphosphoribosyl |
| Farn | farnesylation |
| Gerger | geranylgeranylation |
| Glyco | glycosylation |
| Hy | hydroxylation |
| ISG | ISGylation, ISG15-protein conjugation |
| Me | methylation |
| Me1 | monomethylation, mono-methylation |
| Me2 | dimethylation, di-methylation |
| Me3 | trimethylation, tri-methylation |
| Myr | myristoylation |
| Nedd | neddylation |
| NGlyco | N-linked glycosylation |
| NO | Nitrosylation |
| OGlyco | O-linked glycosylation |
| Palm | palmitoylation |
| Ph | phosphorylation |
| Sulf | sulfation, sulphation, sulfur addition, sulphur addition, sulfonation, sulphonation |
| Sumo | SUMOylation |
| Ub | ubiquitination, ubiquitinylation, ubiquitylation |
| UbK48 | Lysine 48-linked polyubiquitination |
| UbK63 | Lysine 63-linked polyubiquitination |
| UbMono | monoubiquitination |
| UbPoly | polyubiquitination |

### Supported One- and Three-letter Amino Acid Codes

| **Amino Acid** | **1-Letter Code** | **3-Letter Code** |
| -------------- | ----------------- | ----------------- |
| Alanine | A | Ala |
| Arginine | R | Arg |
| Asparagine | N | Asn |
| Aspartic Acid | D | Asp |
| Cysteine | C | Cys |
| Glutamic Acid | E | Glu |
| Glutamine | Q | Gln |
| Glycine | G | Gly |
| Histidine | H | His |
| Isoleucine | I | Ile |
| Leucine | L | Leu |
| Lysine | K | Lys |
| Methionine | M | Met |
| Phenylalanine | F | Phe |
| Proline | P | Pro |
| Serine | S | Ser |
| Threonine | T | Thr |
| Tryptophan | W | Trp |
| Tyrosine | Y | Tyr |
| Valine | V | Val |




### Function Signatures

##### proteinModification(StrArgNSArg, StrArgNSArg?, StrArg?)

1. Namespace argument or default namespace argument (without prefix) of following type(s): ProteinModification

1. Zero or one amespace argument or default namespace argument (without prefix) of following type(s): AminoAcid

1. Zero or one string argument of following type(s): /\d+/



### Examples


default BEL namespace and 1-letter amino acid code

    p(HGNC:AKT1, pmod(Ph, S, 473))


default BEL namespace and 3-letter amino acid code

    p(HGNC:AKT1, pmod(Ph, Ser, 473))


[PSI-MOD](http://psidev.cvs.sourceforge.net/viewvc/psidev/psi/mod/data/PSI-MOD.obo) namespace and 3-letter amino acid code


    p(HGNC:AKT1, pmod(MOD:PhosRes, Ser, 473))


MAPK1 phosphorylated at both Threonine 185 and Tyrosine 187

    p(HGNC:MAPK1, pmod(Ph, Thr, 185), pmod(Ph, Tyr, 187))


HRAS palmitoylated at an unspecified residue using default BEL namespace

    p(HGNC:HRAS, pmod(Palm))



---
##### [Request an Edit](https://github.com/belbio/bel_lang_ws/issues/new?title=Doc edit request - proteinModification (2.0.0))