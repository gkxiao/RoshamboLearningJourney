![ROS1 inhibitor compound 31](data/AZ-ROS1-inhibitor-31.png)

**Figure 1.** Compound 31

**31.sdf** is a ROS1 inhibitor hit ( compound 13 ) discovered by Petrović, D. et al. (2022) through Fragment-Based Drug Discovery (FBDD). In this exercise, it serves as the **query** for ROSHAMBO2. Compound 13 underwent structure preparation using Flare, followed by conformational searching and alignment via the "Conf Hunt & Align" module. This process generated the bioactive conformation by aligning the compound to the ligands in three ROS1 co-crystal structures (PDB: 3ZBF, 4UXL, 7Z5X).

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
| count | 10000.000000 | 10000.000000 | 10000.000000 | 10000.000000 |
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



### Table 2. Six main score values of CHEMBL1997924

| Metric | Value |
|-----------------------|-----------|
| tanimoto_combo_legacy | 1.430 |
| tanimoto_combination | 0.715 |
| FitTversky_volume | 0.864 |
| FitTversky_color | 0.651 |
| RefTverskyCombo | 1.873 |
| FitTverskyCombo | 1.515 |

## Reference
1. Petrović, D. et al. (2022) “Virtual Screening in the Cloud Identifies Potent and Selective ROS1 Kinase Inhibitors,” Journal of Chemical Information and Modeling, 62(16), pp. 3832–3843. Available at: https://doi.org/10.1021/acs.jcim.2c00644.

