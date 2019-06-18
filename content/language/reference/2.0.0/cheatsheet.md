---
title: BEL Language Cheatsheet

aliases:
- /language/reference/current/cheatsheet

---
<!-- COMPUTER GENERATED PAGE!!! DO NOT EDIT DIRECTLY  -->
<!--    must be changed in scripts/templates.py which is processed by scripts/update_refs.py -->

## BEL Language Cheatsheet (version 2.0.0)

### Functions


#### abundance (a)


##### abundance(NSArg, loc()?)

1. Namespace argument of following type(s): Abundance

1. Zero or one of each function(s): location




#### activity (act)


##### activity(g|r|m|p|complex(), ma()?)

1. One of following function(s): geneAbundance, rnaAbundance, microRNAAbundance, proteinAbundance, complexAbundance

1. Zero or one of each function(s): molecularActivity




#### biologicalProcess (bp)


##### biologicalProcess(NSArg)

1. Namespace argument of following type(s): BiologicalProcess




#### cellSecretion (sec)


##### cellSecretion(p|complex|a())

1. One of following function(s): proteinAbundance, complexAbundance, abundance




#### cellSurfaceExpression (surf)


##### cellSurfaceExpression(p|complex|a())

1. One of following function(s): proteinAbundance, complexAbundance, abundance




#### complexAbundance (complex)


##### complexAbundance(a|p|g|m|r()*, NSArg*, loc()?)

1. Zero or more of each function(s): abundance, proteinAbundance, geneAbundance, microRNAAbundance, rnaAbundance

1. Zero or more namespace arguments of following type(s): Complex

1. Zero or one of each function(s): location




#### compositeAbundance (composite)


##### compositeAbundance(a|act|p|g|m|r|complex()*, NSArg*)

1. Zero or more of each function(s): abundance, activity, proteinAbundance, geneAbundance, microRNAAbundance, rnaAbundance, complexAbundance

1. Zero or more namespace arguments of following type(s): Complex




#### degradation (deg)


##### degradation(p|complex|m|r())

1. One of following function(s): proteinAbundance, complexAbundance, microRNAAbundance, rnaAbundance




#### fragment (frag)


##### fragment(StrArg, StrArg)

1. String argument of following type(s): /[\d\_\?\*]+/

1. String argument of following type(s): /.*?/




#### fusion (fus)


##### fusion(NSArg, StrArg, NSArg, StrArg)

1. Namespace argument of following type(s): Gene, RNA, Micro_RNA, Protein

1. String argument of following type(s): /\S+/

1. Namespace argument of following type(s): Gene, RNA, Micro_RNA, Protein

1. String argument of following type(s): /\S+/




#### geneAbundance (g)


##### geneAbundance(NSArg, loc()?, var()*)

1. Namespace argument of following type(s): Gene

1. Zero or one of each function(s): location

1. Zero or more of each function(s): variant


##### geneAbundance(fus(), loc()?, var()*)

1. One of following function(s): fusion

1. Zero or one of each function(s): location

1. Zero or more of each function(s): variant




#### location (loc)


##### location(NSArg)

1. Namespace argument of following type(s): Location




#### microRNAAbundance (m)


##### microRNAAbundance(NSArg, loc()?, var()*)

1. Namespace argument of following type(s): Micro_RNA

1. Zero or one of each function(s): location

1. Zero or more of each function(s): variant


##### microRNAAbundance(fus(), loc()?, var()*)

1. One of following function(s): fusion

1. Zero or one of each function(s): location

1. Zero or more of each function(s): variant




#### molecularActivity (ma)


##### molecularActivity(StrArgNSArg)

1. Namespace argument or default namespace argument (without prefix) of following type(s): Activity




#### pathology (path)


##### pathology(NSArg)

1. Namespace argument of following type(s): Pathology




#### proteinAbundance (p)


##### proteinAbundance(NSArg, loc|frag()?, var|pmod()*)

1. Namespace argument of following type(s): Protein

1. Zero or one of each function(s): location, fragment

1. Zero or more of each function(s): variant, proteinModification


##### proteinAbundance(fus(), loc()?, var()*)

1. One of following function(s): fusion

1. Zero or one of each function(s): location

1. Zero or more of each function(s): variant




#### proteinModification (pmod)


##### proteinModification(StrArgNSArg, StrArgNSArg?, StrArg?)

1. Namespace argument or default namespace argument (without prefix) of following type(s): ProteinModification

1. Zero or one amespace argument or default namespace argument (without prefix) of following type(s): AminoAcid

1. Zero or one string argument of following type(s): /\d+/




#### reaction (rxn)


##### reaction(reactants(), products())

1. One of following function(s): reactants

1. One of following function(s): products




#### rnaAbundance (r)


##### rnaAbundance(NSArg, loc()?, var()*)

1. Namespace argument of following type(s): RNA

1. Zero or one of each function(s): location

1. Zero or more of each function(s): variant


##### rnaAbundance(fus(), loc()?, var()*)

1. One of following function(s): fusion

1. Zero or one of each function(s): location

1. Zero or more of each function(s): variant




#### translocation (tloc)


##### translocation(g|p|r|m|complex|a(), fromLoc(), toLoc())

1. One of following function(s): geneAbundance, proteinAbundance, rnaAbundance, microRNAAbundance, complexAbundance, abundance

1. One of following function(s): fromLoc

1. One of following function(s): toLoc




#### variant (var)


##### variant(StrArg)

1. String argument of following type(s): /\S+/





### Relations

##### analogous (analogous)

##### association (--)

##### biomarkerFor (biomarkerFor)

##### causesNoChange (cnc)

##### decreases (-|)

##### directlyDecreases (=|)

##### directlyIncreases (=>)

##### hasActivity (hasActivity)

##### hasComponent (hasComponent)

##### hasComponents (hasComponents)

##### hasMember (hasMember)

##### hasMembers (hasMembers)

##### increases (->)

##### isA (isA)

##### negativeCorrelation (neg)

##### orthologous (orthologous)

##### positiveCorrelation (pos)

##### prognosticBiomarkerFor (prognosticBiomarkerFor)

##### rateLimitingStepOf (rateLimitingStepOf)

##### regulates (reg)

##### subProcessOf (subProcessOf)

##### transcribedTo (:>)

##### translatedTo (>>)


---
##### [Request an Edit](https://github.com/belbio/bel_lang_ws/issues/new?title=Doc edit request - translatedTo (2.0.0))