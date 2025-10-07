![ROS1 inhibitor compound 31](data/AZ-ROS1-inhibitor-31.png)

**Figure 1.** Compound 31

**Compound 31** is a ROS1 inhibitor hit ( compound 13 ) discovered by Petrović, D. et al. (2022) through Fragment-Based Drug Discovery (FBDD). In this exercise, it serves as the **query** for [ROSHAMBO2](https://github.com/molecularinformatics/roshambo2). Compound 13 underwent structure preparation using Flare, followed by conformational searching and alignment via the "Conf Hunt & Align" module. This process generated the bioactive conformation by aligning the compound to the ligands in three ROS1 co-crystal structures (PDB: 3ZBF, 4UXL, 7Z5X).

A primary reason for selecting compound 31 as the test case is that no similar compounds have been identified yet in CHEMBL35. CHEMBL35 molecules are characterized by Morgan fingerprints with a radius of 2 and 2048 bits in length. As of writing this post (2025-10-07), no compounds with Tanimoto similarity ≥ 0.4 (this is a widely accepted similarity threshold standard) could be found via [search](https://www.ebi.ac.uk/chembl/advanced_search/similarity/Cc1cc(Nc2nccs2)nc(N(C)Cc2ccc(C%23N)c(Cl)c2)n1/40).

Compound 13 was discovered by Petrović, D. et al. from AstraZeneca (AZ) through searching AZ's internal database using FastROCS shape technology. FastROCS is the GPU version of ROCS, while the shape technology behind ROSHAMBO2 is an imitation of ROCS. We are unable to reproduce Petrović, D. et al.'s computational process using the same database, but we can conduct indirect verification through a reverse screening approach. Therefore, one objective of this study is to examine whether ROSHAMBO2 can predict, based on Compound 13, its 3D structural similarity to known ROS1 inhibitors, and consequently predict that ROS1 is one of its targets.

**chembl35_conf25_hits.sdf** is the top 10000 hits of screeninging against CHEMBL35 with ROSHAMBO2 using **31.sdf** as the query, with the following parameters:

- `--color true`
- `--start_mode 1`
- `--optim_mode combination`
- `--max_results 10000`
- `--n_gpus 2`

**chembl35_conf25_hits_score.csv** contains the virtual screening scoring results. In addition to ROSHAMBO2 scores, Tversky similarity scores have been included, comprising a total of 6 columns:

- RefTversky_volume
- RefTversky_color
- RefTverskyCombo
- FitTversky_volume
- FitTversky_color
- FitTverskyCombo

**CHEMBL35_conf25.h5** is a ROSHAMBO2 H5 format 3D conformational database prepared from CHEMBL V35 drug-like compounds. Conformations were generated using CDPKit's confgen, with up to 25 conformers per molecule. The results are summarized as follows:

- **mol count**: 910625
- **expanded mol count**: 1352233
- **conf count**: 27798929

Where:
- **mol count** refers to the number of compounds obtained from CHEMBL35 before ligand preparation;
- **expanded mol count** refers to the number of molecules after ligand preparation, including expansion due to protonation states, tautomers, and stereoisomers;
- **conf count** refers to the total number of conformations.

## Result

In this virtual screening, ROSHAMBO2 retained a total of 10,000 results with the highest Tanimoto_combination scores. The statistics for the four main combination scores are presented in Table 1.

### Table 1. The statistics for the four main combination scores

| Items | tanimoto_combo_legacy | tanimoto_combination | RefTverskyCombo | FitTverskyCombo |
| :---- | --------------------: | -------------------: | --------------: | --------------: |
| count | 10000 | 10000 | 10000 | 10000 |
| mean | 1.206140 | 0.603070 | 1.492139 | 1.522523 |
| std | 0.050101 | 0.025050 | 0.113713 | 0.125077 |
| min | 1.154999 | 0.577500 | 1.183000 | 1.218000 |
| 25% | 1.170987 | 0.585493 | 1.413000 | 1.434000 |
| 50% | 1.191708 | 0.595854 | 1.483000 | 1.513000 |
| 75% | 1.225248 | 0.612624 | 1.565000 | 1.599000 |
| max | 1.567736 | 0.783868 | 1.978000 | 2.106000 |

Among these results, I am interested in the virtual screening hit compound CHEMBL1997924. The 3D structures of the query and the hit are shown in Figure 2.

![Compound 31 and CHEMBL1997924](https://github.com/gkxiao/RoshamboLearningJourney/blob/main/data/compound-31-and-CHEMBL1997924.png)
**Figure 2.** 3D structures of Compound 31 (left) versus CHEMBL1997924 (right)


Table 2 shows the 3D similarity score values between compound CHEMBL1997924 and compound 31. The tanimoto_shape score of 0.794 indicates visually apparent shape similarity, while tanimoto_combo_legacy = 1.43 and RefTverskyCombo = 1.873 are empirically considered sufficiently high. Ranked by RefTverskyCombo, the compound is tied at 13th position, and ranks 56th by index. Overall, CHEMBL1997924 is readily noticeable based on its score values, particularly given its ROS1 IC50 = 1 nM.

### Table 2. Eight main score values of CHEMBL1997924

| Metric | Value |
|-----------------------|-----------|
| tanimoto_combo_legacy | 1.430 |
| tanimoto_shape | 0.794 |
| tanimoto_color | 0.636 |
| tanimoto_combination | 0.715 |
| FitTversky_volume | 0.864 |
| FitTversky_color | 0.651 |
| RefTverskyCombo | 1.873 |
| FitTverskyCombo | 1.515 |

Additionally, this computation utilized two RTX 4090 GPUs, collectively completing in 12 minutes. This equates to a processing speed of 19,305 conformations/second per GPU. While this speed is significantly lower than the 60,600 conformations/second (on-demand mode) reported in literature, the total runtime of 12 minutes remains acceptable.

## Conclusion
This study successfully demonstrated the utility of ROSHAMBO2 as a virtual screening tool for identifying structurally similar compounds to known ROS1 inhibitors. Using Compound 31 as a query molecule—a ROS1 inhibitor with no structural analogs (Tanimoto similarity ≥ 0.4) in CHEMBL35—we conducted a comprehensive 3D similarity screening against the CHEMBL35 database.

The screening results revealed CHEMBL1997924 as a top-ranking hit with significant 3D similarity to Compound 31, evidenced by high similarity scores including tanimoto_shape (0.794), tanimoto_combo_legacy (1.43), and RefTverskyCombo (1.873). The identification of CHEMBL1997924 is particularly meaningful given its known potent ROS1 inhibitory activity (IC50 = 1 nM), which validates ROSHAMBO2's capability to predict not only structural similarity but also potential target relevance.

The computational efficiency of the screening process, completing in just 12 minutes using two RTX 4090 GPUs, demonstrates the practical utility of ROSHAMBO2 for drug discovery applications. Despite processing at a lower rate (19,305 conformations/second per GPU) than previously reported benchmarks, the total runtime remains acceptable for rapid virtual screening campaigns.

These findings confirm that ROSHAMBO2 can effectively identify compounds with 3D structural similarity to known bioactive molecules, even when traditional 2D fingerprint methods fail to detect similarities. This case study illustrates the value of shape-based screening approaches in fragment-based drug discovery and target prediction, particularly for identifying novel chemical matter with potential therapeutic activity against specific targets like ROS1.

## Reference
1. Petrović, D. et al. (2022) “Virtual Screening in the Cloud Identifies Potent and Selective ROS1 Kinase Inhibitors,” Journal of Chemical Information and Modeling, 62(16), pp. 3832–3843. Available at: https://doi.org/10.1021/acs.jcim.2c00644.

2. ROSHAMBO2. https://github.com/molecularinformatics/roshambo2

3. Atwi, R. et al. (2025) “ROSHAMBO2: Accelerating Molecular Alignment for Large Chemical Libraries with GPU Optimization and Algorithmic Advances,” Journal of Chemical Information and Modeling [Preprint]. Available at: https://doi.org/10.1021/acs.jcim.5c01322.
