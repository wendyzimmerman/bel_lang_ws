
---
title: BEL Language Cheatsheet

---
<!-- COMPUTER GENERATED PAGE!!! DO NOT EDIT DIRECTLY  -->
<!--    must be changed in scripts/templates.py which is processed by scripts/update_refs.py -->

## BEL Language Cheatsheet (version 2.1.0)

### Functions


#### abundance (a)
: Denotes the abundance of an entity.

['abundance(NSArg, loc()?)']

* ['Namespace argument of following type(s): Abundance', 'Zero or one of each function(s): location']



#### activity (act)
: Denotes the frequency or abundance of events in which a member acts as a causal agent at the molecular scale.

['activity(g|r|m|p|complex(), ma()?)']

* ['One of following function(s): geneAbundance, rnaAbundance, microRNAAbundance, proteinAbundance, complexAbundance', 'Zero or one of each function(s): molecularActivity']



#### biologicalProcess (bp)
: Denotes a process or population of events.

['biologicalProcess(NSArg)']

* ['Namespace argument of following type(s): BiologicalProcess']



#### cellSecretion (sec)
: Denotes the frequency or abundance of events in which members of an abundance move from cells to regions outside of the cells.

['cellSecretion(p|complex|a())']

* ['One of following function(s): proteinAbundance, complexAbundance, abundance']



#### cellSurfaceExpression (surf)
: Denotes the frequency or abundance of events in which members of an abundance move to the surface of cells.

['cellSurfaceExpression(p|complex|a())']

* ['One of following function(s): proteinAbundance, complexAbundance, abundance']



#### complexAbundance (complex)
: Denotes the abundance of a molecular complex.

['complexAbundance(a|p|g|m|r|pop()*, NSArg*, loc()?)']

* ['Zero or more of each function(s): abundance, proteinAbundance, geneAbundance, microRNAAbundance, rnaAbundance, populationAbundance', 'Zero or more namespace arguments of following type(s): Complex', 'Zero or one of each function(s): location']



#### compositeAbundance (composite)
: Denotes the frequency or abundance of events in which members are present.

['compositeAbundance(a|act|p|g|m|r|complex|pop()*, NSArg*)']

* ['Zero or more of each function(s): abundance, activity, proteinAbundance, geneAbundance, microRNAAbundance, rnaAbundance, complexAbundance, populationAbundance', 'Zero or more namespace arguments of following type(s): Complex']



#### degradation (deg)
: Denotes the frequency or abundance of events in which a member is degraded in some way such that it is no longer a member.

['degradation(p|complex|m|r())']

* ['One of following function(s): proteinAbundance, complexAbundance, microRNAAbundance, rnaAbundance']



#### fragment (frag)
: Denotes a protein fragment, e.g., a product of proteolytic cleavage.

['fragment(StrArg, StrArg)']

* ['String argument of following type(s): /[\\d\\_\\?\\*]+/', 'String argument of following type(s): /.*?/']



#### fusion (fus)
: Indicates this is a fusion of a gene, RNA, microRNA or protein

['fusion(NSArg, StrArg, NSArg, StrArg)']

* ['Namespace argument of following type(s): Gene, RNA, Micro_RNA, Protein', 'String argument of following type(s): /\\S+/', 'Namespace argument of following type(s): Gene, RNA, Micro_RNA, Protein', 'String argument of following type(s): /\\S+/']



#### geneAbundance (g)
: Denotes the abundance of a gene.

['geneAbundance(NSArg, loc()?, var()*)', 'geneAbundance(fus(), loc()?, var()*)']

* ['Namespace argument of following type(s): Gene', 'Zero or one of each function(s): location', 'Zero or more of each function(s): variant']

* ['One of following function(s): fusion', 'Zero or one of each function(s): location', 'Zero or more of each function(s): variant']



#### location (loc)
: Denotes the cellular location of the abundance.

['location(NSArg)']

* ['Namespace argument of following type(s): Location']



#### microRNAAbundance (m)
: Denotes the abundance of a processed, functional microRNA

['microRNAAbundance(NSArg, loc()?, var()*)', 'microRNAAbundance(fus(), loc()?, var()*)']

* ['Namespace argument of following type(s): Micro_RNA', 'Zero or one of each function(s): location', 'Zero or more of each function(s): variant']

* ['One of following function(s): fusion', 'Zero or one of each function(s): location', 'Zero or more of each function(s): variant']



#### molecularActivity (ma)
: molecular activity type

['molecularActivity(StrArgNSArg)']

* ['Namespace argument or default namespace argument (without prefix) of following type(s): Activity']



#### pathology (path)
: Denotes a disease or pathology process

['pathology(NSArg)']

* ['Namespace argument of following type(s): Pathology']



#### proteinAbundance (p)
: Denotes the abundance of a protein

['proteinAbundance(NSArg, loc|frag()?, var|pmod()*)', 'proteinAbundance(fus(), loc()?, var()*)']

* ['Namespace argument of following type(s): Protein', 'Zero or one of each function(s): location, fragment', 'Zero or more of each function(s): variant, proteinModification']

* ['One of following function(s): fusion', 'Zero or one of each function(s): location', 'Zero or more of each function(s): variant']



#### proteinModification (pmod)
: Post-translational protein modifications

['proteinModification(StrArgNSArg, StrArgNSArg?, StrArg?)']

* ['Namespace argument or default namespace argument (without prefix) of following type(s): ProteinModification', 'Zero or one amespace argument or default namespace argument (without prefix) of following type(s): AminoAcid', 'Zero or one string argument of following type(s): /\\d+/']



#### reaction (rxn)
: Denotes the frequency or abundance of events in a reaction

['reaction(reactants(), products())']

* ['One of following function(s): reactants', 'One of following function(s): products']



#### rnaAbundance (r)
: Denotes the abundance of an RNA

['rnaAbundance(NSArg, loc()?, var()*)', 'rnaAbundance(fus(), loc()?, var()*)']

* ['Namespace argument of following type(s): RNA', 'Zero or one of each function(s): location', 'Zero or more of each function(s): variant']

* ['One of following function(s): fusion', 'Zero or one of each function(s): location', 'Zero or more of each function(s): variant']



#### translocation (tloc)
: Denotes the frequency or abundance of events in which members move between locations

['translocation(g|p|r|m|complex|pop|a(), fromLoc(), toLoc())']

* ['One of following function(s): geneAbundance, proteinAbundance, rnaAbundance, microRNAAbundance, complexAbundance, populationAbundance, abundance', 'One of following function(s): fromLoc', 'One of following function(s): toLoc']



#### variant (var)
: Denotes a sequence variant

['variant(StrArg)']

* ['String argument of following type(s): /\\S+/']



### Relations

##### analogous (analogous)

##### association (--)

##### biomarkerFor (biomarkerFor)

##### causesNoChange (cnc)

##### decreases (-|)

##### directlyDecreases (=|)

##### directlyIncreases (=>)

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
