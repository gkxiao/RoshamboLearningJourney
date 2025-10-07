![ROS1 inhibitor compound 31](data/AZ-ROS1-inhibitor-31.png)

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

## Reference
1. Petrović, D. et al. (2022) “Virtual Screening in the Cloud Identifies Potent and Selective ROS1 Kinase Inhibitors,” Journal of Chemical Information and Modeling, 62(16), pp. 3832–3843. Available at: https://doi.org/10.1021/acs.jcim.2c00644.

