# The Impact of Query Molecule Preparation on Shape-Based Virtual Screening

## Abstract

Shape-based virtual screening has emerged as a powerful strategy for identifying structurally novel bioactive compounds from ultra-large chemical libraries. However, the performance of such approaches is highly sensitive to the conformational state of the query molecule. In this study, we investigate the influence of query conformation preparation on virtual screening outcomes using compound 31—a ROS1-selective inhibitor recently reported by AstraZeneca—as a model system. Through quantum mechanical optimization and structural alignment with multiple ROS1 co-crystal ligands (PDB: 3ZBF, 4UXL, 7Z5X, 7Z5W), we identified a low-energy bioactive conformation (CONF_34) that recapitulates key hinge- and DFG-region interactions observed in the protein–ligand complex. In contrast, a high-energy non-bioactive conformation (CONF_17, ΔE = 8.5 kcal/mol) was selected to represent an energetically inaccessible state. Both conformers were used as queries in shape-based virtual screening against a curated 3D conformational ensemble derived from ChEMBL35 (∼1.35 million compounds, ∼27.8 million conformers), employing the ROSHAMBO2 platform with Tanimoto and Tversky similarity metrics. While global score distributions were comparable, the bioactive conformation significantly outperformed the non-bioactive one in retrieving known ROS1 inhibitors: the high-affinity hit CHEMBL1997924 (*K*<sub>i</sub> = 1 nM) ranked 11th (RefTverskyCombo = 1.88) with CONF_34 versus 50th (RefTverskyCombo = 1.81) with CONF_17 under standard competition ranking. Moreover, Tversky-based scoring (α = 0.95) demonstrated superior ranking performance over conventional Tanimoto combination scores. These results underscore that query conformation selection is not merely a preprocessing step but a critical determinant of virtual screening efficacy. We advocate for the integration of bioactive conformations in shape-based screening workflows to enhance the early identification of novel, high-quality hit compounds.

## Keywords

shape-based virtual screening; query conformation; ROS1 kinase inhibitor; bioactive conformation; ROSHAMBO2; Tversky similarity; ChEMBL; quantum mechanical optimization; molecular shape; computational drug discovery

---

## 1. Introduction

Petrović et al. from AstraZeneca<sup>1</sup> reported a large-scale virtual screening campaign leveraging OpenEye FastROCS<sup>2</sup>, deployed across hundreds of GPUs in the cloud, to interrogate a 10<sup>10</sup>-member subset of AstraZeneca’s virtual compound library. The authors subsequently enumerated structural analogs around identified hit scaffolds, exploring a virtual chemical space encompassing ∼10<sup>15</sup> molecules. Hit compounds from FastROCS screening were subjected to molecular docking, leading to the synthesis and biological evaluation of two series as inhibitors of ROS1 and TrkA kinases. This work demonstrated the feasibility and practical utility of shape-based similarity methods<sup>3</sup> in discovering novel, potent, and selective kinase inhibitors from ultra-large chemical spaces.

![ROS1 inhibitor compound 31](http://blog.molcalx.com.cn/wp-content/uploads/2025/10/AZ-ROS1-inhibitor-31.png){width=198 height=183 .aligncenter}

**Figure 1.** Chemical structure of compound 31.

Among the identified hits, compound 31 (Figure 1) emerged as a representative ROS1-selective inhibitor, exhibiting an IC<sub>50</sub> of 97 nM against ROS1 and >100 μM against TrkA, thereby demonstrating exceptional kinase selectivity. Notably, as of the time of writing, a similarity search in the ChEMBL database<sup>4</sup> using compound 31 as the query (Morgan fingerprint, radius = 2, 2048 bits; Tanimoto coefficient ≥ 0.4) yielded no structurally analogous known compounds. This observation further highlights the capacity of shape-based virtual screening to uncover chemotypes with high structural novelty.

The preparation strategy for the query molecule critically influences the outcome of shape-based virtual screening. Extensive literature has examined the performance of leading shape-matching tools such as ROCS<sup>5</sup>, as previously reviewed by our group<sup>6</sup>. Herein, we use the discovery of compound 31 as a case study to systematically evaluate the impact of query conformation selection on virtual screening results. Given that the original screening library is not publicly accessible and the computational resources required for full replication are prohibitive, we instead adopt compound 31 as the query and perform virtual screening against the ChEMBL database. Our objective is to assess how different query preparation protocols affect the retrieval and ranking of known ROS1 inhibitors.

## 2. Results and Discussion

### 2.1 Query Conformation Preparation: Identification of the Bioactive Conformation

We selected the co-crystallized ligands from four ROS1 structures (PDB IDs: 3ZBF, 4UXL, 7Z5X, 7Z5W) reported by Petrović et al.<sup>1</sup> as reference molecules. Compound 31 was aligned to these references using the Conf Hunt & Align module in Flare (Cresset), employing the “Accurate but slow” setting.

To ensure conformational energetics were physically reasonable, all generated conformers underwent quantum mechanical (QM) refinement. Geometry optimization was first performed at the GFN2-xTB level, followed by single-point energy calculations at the R2SCAN-3c//def2-mTZVPP level. Conformers were clustered using an RMSD threshold of 0.125 Å, yielding a representative subset of 133 low-energy conformations (see Supporting Information: `31_CONFS_QM.sdf`).

![Overlay of compound 31 with ROS1 co-crystal ligands](http://blog.molcalx.com.cn/wp-content/uploads/2025/10/bioactive-conformer-CONF_34.png){width=1065 height=687 .aligncenter}

**Figure 2.** Three-dimensional overlay of compound 31 (yellow) with ligands from four ROS1 co-crystal structures (PDB: 3ZBF, 4UXL, 7Z5X, 7Z5W). Smi denotes the Flare XED field similarity score.

Given the shared hinge-binding motif between compound 31 and the ligand in PDB 7Z5W, the overlay shows perfect superposition of this common substructure (Figure 2, bottom right), with a high overall similarity score (Sim > 0.74). Systematic analysis revealed seven low-energy conformers (energies: 0.836–1.137 kcal/mol; IDs: CONF_30, 34, 45, 48, 36, 41, 46) that consistently aligned with the 7Z5W ligand. These were grouped into two representative clusters, exemplified by CONF_34 and CONF_41, differing primarily in the spatial orientation of the chlorine atom due to rotation of the 3-chloro-4-cyanophenyl ring. Figure 2 (bottom right) illustrates CONF_34.

Further overlays with ligands from PDB 3ZBF, 4UXL, and 7Z5X confirmed that CONF_34/41 also achieve favorable alignment with these co-crystal structures (Figure 2).

![Binding mode comparison in the hinge region](http://blog.molcalx.com.cn/wp-content/uploads/2025/10/Compound-31-CONF_41-binding-mode-hinge-interaction-rev1.png){width=1155 height=602 .aligncenter}

**Figure 3.** Comparison of binding modes in the ROS1 hinge region (PDB 7Z5W). The protein backbone is shown as a ribbon; the hinge region is colored red, and the DFG motif is colored cyan. Compound 31 is depicted in yellow; the co-crystal ligand is in purple.

Analysis of the binding pose of compound 31 within the ROS1 pocket (based on PDB 7Z5W) reveals that it recapitulates the key interactions of the co-crystal ligand in the hinge region (Figure 3). The thiazole, pyrimidine, and intervening NH group adopt a near-coplanar arrangement, stabilized by an S···N hyperconjugative effect. Specifically, the thiazole nitrogen acts as a hydrogen bond acceptor with the backbone NH of Met2029, while the bridging NH serves as a donor to the carbonyl oxygen of the same residue. Additionally, C–H groups on both aromatic rings engage in weak C–H···O=C interactions with the carbonyl oxygens of Glu2027 and Glu2030.

![Binding mode comparison in the DFG region](http://blog.molcalx.com.cn/wp-content/uploads/2025/10/Compound-31-CONF_41-binding-mode-in-DFG-motif.png){width=1161 height=621 .aligncenter}

**Figure 4.** Comparison of binding modes in the DFG region (PDB 7Z5W). Coloring scheme as in Figure 3.

As shown in Figure 4, the 3-chloro-4-cyanophenyl moiety of compound 31 spatially overlaps with the isoxazole group of the co-crystal ligand. The para-cyano group extends toward the DFG motif (cyan ribbon), with its nitrogen atom occupying a position equivalent to a nitrogen in the co-crystal ligand’s pyridazine ring, forming a strong hydrogen bond with the backbone NH of Asp2012.

The N,N-dimethylamino linker connecting the hinge- and DFG-binding fragments of compound 31 aligns precisely with the tetrahydropyrrole ring of the co-crystal ligand (Figure 4), effectively serving as an acyclic bioisostere.

Collectively, the identified conformation of compound 31 exhibits hallmark features of a bioactive state: (1) low conformational strain energy; (2) high shape and electrostatic similarity to the PDB 7Z5W ligand (Sim = 0.77); (3) faithful reproduction of critical protein–ligand interactions in both hinge and DFG regions; and (4) effective mimicry of the co-crystal ligand’s linker geometry. These attributes support its use as a reliable query conformation in subsequent virtual screening experiments.

### 2.2 Design of a Non-Bioactive Conformation

To evaluate the impact of non-bioactive conformations, we selected CONF_17—a high-energy conformation excluded during bioactive conformation identification—as a representative non-bioactive state. CONF_17 exhibits two key characteristics: (1) energetic inaccessibility, with a conformational strain energy of 8.5 kcal/mol (computed at B3LYP-D3BJ/6-31+G(d)//GFN2-xTB); and (2) significant structural deviation from the putative bioactive conformation CONF_34, as illustrated in Figure 5. Specifically, the thiazole ring undergoes a flip, the 3-chloro-4-cyanophenyl group rotates about its aryl–aryl bond, and the N,N-dimethyl linker adopts a non-planar conformation.

![Comparison of bioactive (CONF_34) and non-bioactive (CONF_17) conformations](http://blog.molcalx.com.cn/wp-content/uploads/2025/10/active-CONF_34_and_inactive-CONF_17_of-compound-31.png){width=1016 height=452 .aligncenter}

**Figure 5.** Structural comparison between the putative bioactive conformation (CONF_34) and non-bioactive conformation (CONF_17) of compound 31.

### 2.3 Construction of the ChEMBL35 3D Database

The ChEMBL35 database<sup>7</sup> was downloaded in SMILES format and subjected to a multi-step curation pipeline: standardization, desalting, elemental filtering (retaining only C, H, O, N, S, P, and halogens), deduplication, drug-likeness filtering, and removal of reactive functional groups. Protonation states were assigned at pH 7.4, and 3D conformations were generated using the Confgen module in CDPKit<sup>8,9</sup>, with enumeration of undefined stereocenters. Each molecule was represented by up to 25 low-energy conformers. The compound and conformation counts at each processing stage are summarized in Table 1.

| Processing Stage         | Count        |
|--------------------------|--------------|
| Initial compounds        | 910,625      |
| Curated compounds        | 1,352,233    |
| Total generated conformers | 27,798,929 |

**Table 1.** Statistics of compound and conformation counts during ChEMBL35 database curation.

### 2.4 Virtual Screening

Virtual screening was performed using the recently released ROSHAMBO2 platform<sup>10,11</sup>, which implements a shape-matching algorithm conceptually similar to ROCS. Database conformers were rigidly aligned to the query to maximize volumetric overlap. Molecular similarity was quantified using Tanimoto coefficients for shape and pharmacophoric (“color”) features, each ranging from 0 to 1. The sum of these scores—denoted as *Tanimoto_combo_legacy* (Tc)—ranges from 0 to 2. ROSHAMBO2 also provides a normalized variant, *tanimoto_combination*, scaled to [0,1]. Given that Tversky indices often outperform Tanimoto metrics when query and database molecules differ significantly in size<sup>12</sup>, we additionally computed *RefTverskyCombo* (α = 0.95, query-biased) and *FitTverskyCombo* (database-biased) scores.

Screening was conducted separately using CONF_34 (bioactive) and CONF_17 (non-bioactive) as queries, retrieving the top 10,000 hits based on *tanimoto_combination*. For compounds with multiple stereoisomers or tautomers, the entry with the highest *RefTverskyCombo* score was retained as the representative. Hits were then ranked in descending order of similarity to compound 31, and the position of the first known ROS1 inhibitor in this ranked list was recorded.

Descriptive statistics for the top 10,000 hits are presented in Tables 2 and 3. The score distributions for both query conformations are remarkably similar, suggesting that global similarity metrics alone may not distinguish bioactive from non-bioactive queries.

**Table 2.** Descriptive statistics of key combination scores for virtual screening using CONF_34.

| Items                    | Tanimoto Combo (Legacy) | Tanimoto Combination | RefTversky Combo | FitTversky Combo |
|--------------------------|--------------------------|-----------------------|-------------------|-------------------|
| count                    | 10,000                   | 10,000                | 10,000            | 10,000            |
| mean                     | 1.21                     | 0.60                  | 1.49              | 1.52              |
| std                      | 0.05                     | 0.03                  | 0.11              | 0.12              |
| min                      | 1.16                     | 0.58                  | 1.19              | 1.20              |
| 25%                      | 1.17                     | 0.59                  | 1.42              | 1.44              |
| 50%                      | 1.19                     | 0.60                  | 1.49              | 1.52              |
| 75%                      | 1.23                     | 0.61                  | 1.57              | 1.60              |
| max                      | 1.57                     | 0.78                  | 1.97              | 2.11              |

**Table 3.** Descriptive statistics of key combination scores for virtual screening using CONF_17.

| Items                    | Tanimoto Combo (Legacy) | Tanimoto Combination | RefTversky Combo | FitTversky Combo |
|--------------------------|--------------------------|-----------------------|-------------------|-------------------|
| count                    | 10,000                   | 10,000                | 10,000            | 10,000            |
| mean                     | 1.22                     | 0.61                  | 1.54              | 1.50              |
| std                      | 0.04                     | 0.02                  | 0.10              | 0.11              |
| min                      | 1.18                     | 0.59                  | 1.21              | 1.24              |
| 25%                      | 1.19                     | 0.60                  | 1.47              | 1.42              |
| 50%                      | 1.21                     | 0.61                  | 1.54              | 1.48              |
| 75%                      | 1.24                     | 0.62                  | 1.61              | 1.56              |
| max                      | 1.53                     | 0.77                  | 1.96              | 2.10              |

Among the top 10,000 hits, CONF_17 retrieved only one known ROS1 inhibitor:
- **CHEMBL1997924**: Tc = 1.33, RefTc = 1.81, ROS1 *K*<sub>i</sub> = 1 nM

In contrast, CONF_34 identified three:
- **CHEMBL1997924**: Tc = 1.43, RefTc = 1.88, *K*<sub>i</sub> = 1 nM  
- **CHEMBL1970189**: Tc = 1.21, RefTc = 1.68, *K*<sub>i</sub> = 19.95 nM  
- **CHEMBL1983923**: Tc = 1.22, RefTc = 1.49, *K*<sub>i</sub> = 199.53 nM  

This observation suggests that while both conformations can retrieve high-affinity actives, the bioactive conformation demonstrates superior recall capability.

To rigorously assess ranking performance, two ranking schemes were applied using Pandas’ `rank()` function:
1. **min (standard competition ranking)**: Tied entries receive the lowest possible rank; subsequent ranks are skipped.
2. **dense ranking**: Tied entries share the same rank; subsequent ranks remain consecutive.

Notably, regardless of query conformation, the highest-scoring known ROS1 inhibitor was consistently CHEMBL1997924 (*K*<sub>i</sub> = 1 nM).

**Table 4.** Ranking analysis of CHEMBL1997924 using RefTverskyCombo scores.

| Query    | RefTversky Combo | Min Rank | Dense Rank | Index Position |
|----------|------------------|----------|------------|----------------|
| CONF_34  | 1.88             | 11       | 11         | 51             |
| CONF_17  | 1.81             | 50       | 36         | 298            |

Using RefTverskyCombo as the scoring function, CONF_34 achieved a substantially better rank (11th) compared to CONF_17 (50th) under standard competition ranking (Table 4).

**Table 5.** Ranking analysis of CHEMBL1997924 using Tanimoto Combo scores.

| Query    | Tanimoto Combo | Min Rank | Dense Rank | Index Position |
|----------|----------------|----------|------------|----------------|
| CONF_34  | 1.43           | 52       | 52         | 51             |
| CONF_17  | 1.33           | 299      | 298        | 298            |

Similarly, when using Tc as the scoring metric, CONF_34 ranked the hit at position 52, whereas CONF_17 placed it at 299 (Table 5). Furthermore, Tversky-based scoring consistently yielded better early enrichment than Tc, underscoring its advantage in this context.

### 2.5 Limitations of Non-Bioactive Conformations in Hit Retrieval

To understand why CONF_17 still retrieved CHEMBL1997924 despite its non-bioactive nature, we performed a conformational overlay (Figure 6). The alignment reveals substantial spatial overlap: (1) the thiazole–NH–pyrimidine plane of compound 31 aligns well with the pyrazole–NH–thienopyrimidine core of CHEMBL1997924; (2) the aryl rings adopt similar orientations; and (3) the C–N–C linker conformations are compatible. From a purely shape- and pharmacophore-based perspective, this match appears valid.

![Overlay of CONF_17 and CHEMBL1997924](http://blog.molcalx.com.cn/wp-content/uploads/2025/10/CHEMBL1997924-align-to-CONF_17.png){width=958 height=228 .aligncenter}

**Figure 6.** Conformational overlay between the non-bioactive conformation of compound 31 (CONF_17, yellow) and hit compound CHEMBL1997924 (green).

However, deeper analysis reveals critical flaws. The planar arrangement of the pyrazole–NH–thienopyrimidine system in CHEMBL1997924 induces significant electrostatic repulsion between adjacent nitrogen atoms, rendering this conformation energetically unfavorable. Moreover, such a geometry would be incompatible with the ROS1 binding pocket, preventing formation of essential hinge-region hydrogen bonds. Consequently, even if this conformation were sampled during screening, it would likely be discarded during downstream filtering or docking validation. This case illustrates that **geometric similarity alone—without conformational plausibility or binding-mode compatibility—can lead to misleading virtual screening outcomes**.


### 2.6. Implicit Correction of Query Conformation Errors in Cascade Screening Workflows

The findings presented above help explain a common yet often overlooked phenomenon in practical drug discovery: during methodological validation (e.g., using benchmark datasets such as DUD-E), shape- or pharmacophore-based virtual screening methods typically exhibit excellent enrichment performance, effectively discriminating known active compounds from decoys. However, when the same methods are applied to large-scale real-world compound libraries and followed by stringent multi-stage funnel filtering—such as conformational strain energy thresholds, key interaction filters, and other post-processing criteria—the final set of candidate compounds is frequently extremely limited (in many cases, no compounds survive the filters at all), and those that do are often found to lack significant biological activity upon experimental testing.

An even more counterintuitive observation is that cascade virtual screening strategies—comprising an initial shape/pharmacophore filter followed by molecular docking refinement—often yield experimentally validated hit compounds, even when the query molecule has not undergone rigorous conformational preparation (e.g., when a default 3D conformation generated directly from a 2D structure is used). This apparent paradox can be attributed to the implicit error-correction capability of the docking stage within the cascade workflow. Specifically, the first-stage shape or pharmacophore screening acts primarily as a high-throughput feature-matching filter, rapidly eliminating chemically irrelevant regions of chemical space. In contrast, the second-stage molecular docking not only resamples low-energy ligand conformations within the binding pocket but also explicitly evaluates protein–ligand interactions, thereby automatically “correcting” geometric or electrostatic biases inadvertently introduced by a suboptimal initial query conformation. Consequently, even if the starting query conformation is non-bioactive, as long as it retains essential pharmacophoric features, the docking step may still identify a conformation that is both energetically plausible and consistent with the native binding mode, allowing it to pass subsequent stringent filtering steps.

## 3. Materials and Methods

### 3.1 Query Molecule Preparation

Co-crystal structures (PDB: 3ZBF, 4UXL, 7Z5X, 7Z5W) were downloaded from the Protein Data Bank and prepared in Flare v10 using the *Protein Prep* tool to add hydrogens, optimize hydrogen bonding networks, resolve steric clashes, and assign optimal protonation states. Truncated protein chains were capped. Only chain A was retained, and co-crystallized ligands were extracted into a ligand table.

Protein sequences were aligned using *Sequence | Align*, and structures were superimposed onto 3ZBF as the reference via *Sequence | Superimpose*, yielding a structurally aligned set of protein–ligand complexes.

### 3.2 3D Database Preparation from ChEMBL35

The 3D conformational ensemble for ChEMBL35 was generated using CDPKit’s `confgen` module:

```bash
confgen -i chembl35.sdf \
        -o chembl35_confs.sdf \
        -t 60 \
        --max-num-out-confs 25
```

This command implicitly uses the following defaults:

- `-C MEDIUM_SET_DIVERSE`: medium-sized diverse conformation set
- `-c AUTO`: automatic selection of systematic or stochastic sampling
- `-e 15`: retain conformers within 15.0 kcal/mol of the global minimum
- `-r 0.5`: minimum RMSD of 0.5 Å between output conformers
- `-S true`: ignore input 3D coordinates and regenerate conformations
- **Force fields**: MMFF94S_RTOR_NO_ESTAT (systematic), MMFF94S_RTOR (stochastic)


### 3.3 ROSHAMBO2 Virtual Screening
Key ROSHAMBO2 parameters:

backend: cuda
color: true
start_mode: 1
optim_mode: combination
max_results: 10000
n_gpus: 2
Computations were performed on a workstation equipped with two NVIDIA RTX 4090 GPUs.

### 3.4 Statistical Analysis and Ranking
Ranking and statistical analyses were implemented in Python using Pandas. Source code is available at:
https://github.com/gkxiao/RoshamboLearningJourney/blob/main/result_analysis.py

## 4. Conclusion
This study systematically evaluates the impact of query conformation preparation on shape-based virtual screening performance, using the ROS1-selective inhibitor compound 31 as a model system. Through quantum mechanical optimization and structural alignment with multiple ROS1 co-crystal ligands, we identified a low-energy bioactive conformation (CONF_34) that faithfully recapitulates key interactions in both the hinge and DFG regions of the kinase binding pocket. In contrast, a high-energy non-bioactive conformation (CONF_17, ΔE = 8.5 kcal/mol) was used to represent an energetically inaccessible state.

Virtual screening against a curated ChEMBL35 3D database (∼1.35 million compounds) revealed that, despite comparable global score distributions, the bioactive conformation significantly outperformed the non-bioactive one in retrieving and prioritizing known ROS1 inhibitors. The high-affinity compound CHEMBL1997924 (K<sub>i</sub> = 1 nM) ranked 11th with CONF_34 versus 50th with CONF_17 under standard competition ranking using RefTverskyCombo scores. Tversky-based metrics (α = 0.95) consistently demonstrated superior early enrichment over conventional Tanimoto combination scores.

Although the non-bioactive conformation achieved geometric similarity with certain actives, its high energy and binding-mode incompatibility render it unsuitable for guiding meaningful hit discovery. These findings emphasize that query conformation selection is not a mere technical formality but a pivotal factor governing virtual screening success.

We recommend that shape-based screening workflows incorporate bioactive conformations as queries to enhance the identification of novel, high-quality hit compounds. 

## 5. References
1. Petrović, D. et al. (2022) "Virtual Screening in the Cloud Identifies Potent and Selective ROS1 Kinase Inhibitors," *Journal of Chemical Information and Modeling*, 62(16), pp. 3832–3843. Available at: https://doi.org/10.1021/acs.jcim.2c00644.

2. FastROCS. GPU-accelerated Shape Similarity Search. Openeye, Cadence Molecular Sciences. [https://www.eyesopen.com/fastrocs](https://www.eyesopen.com/fastrocs)

3. Nicholls, A. et al. (2010) "Molecular Shape and Medicinal Chemistry: A Perspective," *Journal of Medicinal Chemistry*, 53(10), pp. 3862–3886. Available at: https://doi.org/10.1021/jm900818s.

4. A [similarity search](https://www.ebi.ac.uk/chembl/advanced_search/similarity/Cc1cc(Nc2nccs2)nc(N(C)Cc2ccc(C%23N)c(Cl)c2)n1/40) was conducted on October 9, 2025, using the chemical structure "Cc1cc(Nc2nccs2)nc(N(C)Cc2ccc(C#N)c(Cl)c2)n1" as the query molecule with a similarity threshold of 40% via the ChEMBL database ([https://www.ebi.ac.uk/chembl/advanced_search/similarity/Cc1cc(Nc2nccs2)nc(N(C)Cc2ccc(C%23N)c(Cl)c2)n1/40](https://www.ebi.ac.uk/chembl/advanced_search/similarity/Cc1cc(Nc2nccs2)nc(N(C)Cc2ccc(C%23N)c(Cl)c2)n1/40)). No compounds were retrieved under these search conditions.

5. ROCS. Openeye, Cadence Molecular Sciences. [https://www.eyesopen.com/rocs](https://www.eyesopen.com/rocs)

6. [https://github.com/gkxiao/ROCS-Query-Prep-Benchmark](https://github.com/gkxiao/ROCS-Query-Prep-Benchmark)

7. [https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL35](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL35)

8. CDPKit (Version 1.2.3). [https://github.com/molinfo-vienna/CDPKit](https://github.com/molinfo-vienna/CDPKit)

9. Seidel, T. et al. (2023) "High-Quality Conformer Generation with CONFORGE: Algorithm and Performance Assessment," *Journal of Chemical Information and Modeling*, 63(17), pp. 5549–5570. Available at: https://doi.org/10.1021/acs.jcim.3c00563.

10. Atwi, R. et al. (2025) "ROSHAMBO2: Accelerating Molecular Alignment for Large Chemical Libraries with GPU Optimization and Algorithmic Advances," *Journal of Chemical Information and Modeling* [Preprint]. Available at: https://doi.org/10.1021/acs.jcim.5c01322.

11. Atwi, R. et al. (2024) "ROSHAMBO: Open-Source Molecular Alignment and 3D Similarity Scoring," *Journal of Chemical Information and Modeling*, 64(21), pp. 8098–8104. Available at: https://doi.org/10.1021/acs.jcim.4c01225.

12. G. K. Xiao. Using Tversky in ligand 3D similarity-based virtual screening. Molcalx. [http://blog.molcalx.com.cn/2023/04/17/using-tversky-in-vs.html](http://blog.molcalx.com.cn/2023/04/17/using-tversky-in-vs.html)

---

**Data Availability**: All datasets and scripts used in this study are available at: [https://github.com/gkxiao/RoshamboLearningJourney](https://github.com/gkxiao/RoshamboLearningJourney)
