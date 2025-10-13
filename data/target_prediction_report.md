# 化学基因组学靶标预测分析报告

## 分析概述

- Input: CONF_34_VS_hits_score.csv
- Similarity Metric: RefTverskyCombo
- ChEMBL: Version 35

### 数据统计
- **相似性文件记录数**: 10,000
- **靶标文件记录数**: 6,461
- **构建化合物相似性映射**: 10,000个
- **匹配靶标记录**: 6,461条
- **不同靶标数量**: 792个
- **生成分析结果**: 792个靶标

### 输出文件
- **报告保存位置**: `target_prediction_report.csv`

---

## 分析摘要

### 总体统计
| 指标 | 数值 |
|------|------|
| 总靶标数 | 792 |
| 最高相似性打分 | 1.552455 |
| 最低相似性打分 | 1.200591 |
| 平均相似性打分 | 1.289115 |

### 前10个预测靶标

#### 1. CHEMBL3788 - Serine/threonine-protein kinase PLK4
- **相似性打分**: 1.552455
- **相似性区间**: [1.206659, 1.552455]
- **最佳化合物**: CHEMBL5183478
- **物种**: Homo sapiens

#### 2. CHEMBL3885546 - Corticotropin-releasing factor receptor 2/Corticotropin-releasing factor-binding protein
- **相似性打分**: 1.551882
- **相似性区间**: [1.217596, 1.551882]
- **最佳化合物**: CHEMBL1327614
- **物种**: Homo sapiens

#### 3. CHEMBL2815 - Nerve growth factor receptor Trk-A
- **相似性打分**: 1.526303
- **相似性区间**: [1.207519, 1.526303]
- **最佳化合物**: CHEMBL5201147
- **物种**: Homo sapiens

#### 4. CHEMBL2083 - Fatty acid binding protein adipocyte
- **相似性打分**: 1.519905
- **相似性区间**: [1.207503, 1.519905]
- **最佳化合物**: CHEMBL184142
- **物种**: Homo sapiens

#### 5. CHEMBL251 - Adenosine A2a receptor
- **相似性打分**: 1.519850
- **相似性区间**: [1.200071, 1.519850]
- **最佳化合物**: CHEMBL264433
- **物种**: Homo sapiens

#### 6. CHEMBL226 - Adenosine A1 receptor
- **相似性打分**: 1.519850
- **相似性区间**: [1.202468, 1.519850]
- **最佳化合物**: CHEMBL264433
- **物种**: Homo sapiens

#### 7. CHEMBL3356 - Cytochrome P450 1A2
- **相似性打分**: 1.509808
- **相似性区间**: [1.204396, 1.509808]
- **最佳化合物**: CHEMBL578928
- **物种**: Homo sapiens

#### 8. CHEMBL289 - Cytochrome P450 2D6
- **相似性打分**: 1.509808
- **相似性区间**: [1.201356, 1.509808]
- **最佳化合物**: CHEMBL578928
- **物种**: Homo sapiens

#### 9. CHEMBL2366461 - Cytochrome b6-f complex subunit 4
- **相似性打分**: 1.505382
- **相似性区间**: [1.257829, 1.505382]
- **最佳化合物**: CHEMBL2271292
- **物种**: Spinacia oleracea

#### 10. CHEMBL1844 - Macrophage colony stimulating factor receptor
- **相似性打分**: 1.503744
- **相似性区间**: [1.207519, 1.503744]
- **最佳化合物**: CHEMBL2005449
- **物种**: Homo sapiens

---

## 前20个预测靶标详细信息

### 排名 1
- **靶标ID**: CHEMBL3788
- **靶标名称**: Serine/threonine-protein kinase PLK4
- **物种**: Homo sapiens
- **相似性打分**: 1.552455
- **相似性区间**: [1.206659, 1.552455]
- **平均相似性**: 1.348264
- **化合物数量**: 35
- **最佳化合物ID**: CHEMBL5183478
- **最佳化合物SMILES**: `Cc1cc(Nc2nc(NCc3ccc(Cl)cc3)nc3c2cnn3C)n[nH]1`
- **活性类型**: IC50
- **活性值**: 20.2 nM

### 排名 2
- **靶标ID**: CHEMBL3885546
- **靶标名称**: Corticotropin-releasing factor receptor 2/Corticotropin-releasing factor-binding protein
- **物种**: Homo sapiens
- **相似性打分**: 1.551882
- **相似性区间**: [1.217596, 1.551882]
- **平均相似性**: 1.273549
- **化合物数量**: 10
- **最佳化合物ID**: CHEMBL1327614
- **最佳化合物SMILES**: `Cc1cc(N2CCOCC2)nc(NCc2ccccc2)n1`
- **活性类型**: EC50
- **活性值**: 5680.0 nM

### 排名 3
- **靶标ID**: CHEMBL2815
- **靶标名称**: Nerve growth factor receptor Trk-A
- **物种**: Homo sapiens
- **相似性打分**: 1.526303
- **相似性区间**: [1.207519, 1.526303]
- **平均相似性**: 1.355818
- **化合物数量**: 33
- **最佳化合物ID**: CHEMBL5201147
- **最佳化合物SMILES**: `Cc1cc(Nc2nc(NCc3ccc(C#N)cc3)nc3ccccc23)n[nH]1`
- **活性类型**: IC50
- **活性值**: 83.0 nM

### 排名 4
- **靶标ID**: CHEMBL2083
- **靶标名称**: Fatty acid binding protein adipocyte
- **物种**: Homo sapiens
- **相似性打分**: 1.519905
- **相似性区间**: [1.207503, 1.519905]
- **平均相似性**: 1.373248
- **化合物数量**: 9
- **最佳化合物ID**: CHEMBL184142
- **最佳化合物SMILES**: `CN(Cc1ccc(Cl)cc1)c1nc(O)cc(C(F)(F)F)n1`
- **活性类型**: IC50
- **活性值**: 4000.0 nM

### 排名 5
- **靶标ID**: CHEMBL251
- **靶标名称**: Adenosine A2a receptor
- **物种**: Homo sapiens
- **相似性打分**: 1.519850
- **相似性区间**: [1.200071, 1.519850]
- **平均相似性**: 1.292072
- **化合物数量**: 51
- **最佳化合物ID**: CHEMBL264433
- **最佳化合物SMILES**: `O=C(c1cccs1)c1nc(NCc2ccccc2)nc2ccsc12`
- **活性类型**: Ki
- **活性值**: 25.0 nM

### 排名 6
- **靶标ID**: CHEMBL226
- **靶标名称**: Adenosine A1 receptor
- **物种**: Homo sapiens
- **相似性打分**: 1.519850
- **相似性区间**: [1.202468, 1.519850]
- **平均相似性**: 1.273061
- **化合物数量**: 23
- **最佳化合物ID**: CHEMBL264433
- **最佳化合物SMILES**: `O=C(c1cccs1)c1nc(NCc2ccccc2)nc2ccsc12`
- **活性类型**: Ki
- **活性值**: 1733.0 nM

### 排名 7
- **靶标ID**: CHEMBL3356
- **靶标名称**: Cytochrome P450 1A2
- **物种**: Homo sapiens
- **相似性打分**: 1.509808
- **相似性区间**: [1.204396, 1.509808]
- **平均相似性**: 1.313906
- **化合物数量**: 10
- **最佳化合物ID**: CHEMBL578928
- **最佳化合物SMILES**: `Cc1cc(NC2CCCCC2)nc(NCc2ccccc2)n1`
- **活性类型**: IC50
- **活性值**: 3100.0 nM

### 排名 8
- **靶标ID**: CHEMBL289
- **靶标名称**: Cytochrome P450 2D6
- **物种**: Homo sapiens
- **相似性打分**: 1.509808
- **相似性区间**: [1.201356, 1.509808]
- **平均相似性**: 1.246872
- **化合物数量**: 11
- **最佳化合物ID**: CHEMBL578928
- **最佳化合物SMILES**: `Cc1cc(NC2CCCCC2)nc(NCc2ccccc2)n1`
- **活性类型**: IC50
- **活性值**: 4200.0 nM

### 排名 9
- **靶标ID**: CHEMBL2366461
- **靶标名称**: Cytochrome b6-f complex subunit 4
- **物种**: Spinacia oleracea
- **相似性打分**: 1.505382
- **相似性区间**: [1.257829, 1.505382]
- **平均相似性**: 1.435444
- **化合物数量**: 44
- **最佳化合物ID**: CHEMBL2271292
- **最佳化合物SMILES**: `Cc1nc(N(C=O)Cc2ccc(Cl)cc2)nc(C(F)(F)F)n1`
- **活性类型**: IC50
- **活性值**: 97.72 nM

### 排名 10
- **靶标ID**: CHEMBL1844
- **靶标名称**: Macrophage colony stimulating factor receptor
- **物种**: Homo sapiens
- **相似性打分**: 1.503744
- **相似性区间**: [1.207519, 1.503744]
- **平均相似性**: 1.334170
- **化合物数量**: 5
- **最佳化合物ID**: CHEMBL2005449
- **最佳化合物SMILES**: `Cc1cc(Nc2nc(Cl)cc(NCc3ccccc3)n2)n[nH]1`
- **活性类型**: Ki
- **活性值**: 1258.93 nM

### 排名 11
- **靶标ID**: CHEMBL2185
- **靶标名称**: Serine/threonine-protein kinase Aurora-B
- **物种**: Homo sapiens
- **相似性打分**: 1.880000
- **相似性区间**: [1.412000, 1.880000]
- **平均相似性**: 1.694286
- **化合物数量**: 21
- **最佳化合物ID**: CHEMBL1997924
- **最佳化合物SMILES**: `c1ccc(CNc2nc(Nc3cc(C4CC4)[nH]n3)c3sccc3n2)cc1`
- **活性类型**: Ki
- **活性值**: 125.89 nM

### 排名 12
- **靶标ID**: CHEMBL2971
- **靶标名称**: Tyrosine-protein kinase JAK2
- **物种**: Homo sapiens
- **相似性打分**: 1.880000
- **相似性区间**: [1.374000, 1.880000]
- **平均相似性**: 1.577569
- **化合物数量**: 51
- **最佳化合物ID**: CHEMBL1997924
- **最佳化合物SMILES**: `c1ccc(CNc2nc(Nc3cc(C4CC4)[nH]n3)c3sccc3n2)cc1`
- **活性类型**: Ki
- **活性值**: 1.995 nM

### 排名 13
- **靶标ID**: CHEMBL279
- **靶标名称**: Vascular endothelial growth factor receptor 2
- **物种**: Homo sapiens
- **相似性打分**: 1.880000
- **相似性区间**: [1.388000, 1.880000]
- **平均相似性**: 1.478714
- **化合物数量**: 28
- **最佳化合物ID**: CHEMBL1997924
- **最佳化合物SMILES**: `c1ccc(CNc2nc(Nc3cc(C4CC4)[nH]n3)c3sccc3n2)cc1`
- **活性类型**: Ki
- **活性值**: 31.62 nM

### 排名 14
- **靶标ID**: CHEMBL2041
- **靶标名称**: Tyrosine-protein kinase receptor RET
- **物种**: Homo sapiens
- **相似性打分**: 1.880000
- **相似性区间**: [1.321000, 1.880000]
- **平均相似性**: 1.569571
- **化合物数量**: 7
- **最佳化合物ID**: CHEMBL1997924
- **最佳化合物SMILES**: `c1ccc(CNc2nc(Nc3cc(C4CC4)[nH]n3)c3sccc3n2)cc1`
- **活性类型**: Ki
- **活性值**: 7.943 nM

### 排名 15
- **靶标ID**: CHEMBL3717
- **靶标名称**: Hepatocyte growth factor receptor
- **物种**: Homo sapiens
- **相似性打分**: 1.880000
- **相似性区间**: [1.381000, 1.880000]
- **平均相似性**: 1.622500
- **化合物数量**: 38
- **最佳化合物ID**: CHEMBL1997924
- **最佳化合物SMILES**: `c1ccc(CNc2nc(Nc3cc(C4CC4)[nH]n3)c3sccc3n2)cc1`
- **活性类型**: Ki
- **活性值**: 794.33 nM

### 排名 16
- **靶标ID**: CHEMBL5568
- **靶标名称**: Proto-oncogene tyrosine-protein kinase ROS
- **物种**: Homo sapiens
- **相似性打分**: 1.880000
- **相似性区间**: [1.488000, 1.880000]
- **平均相似性**: 1.681333
- **化合物数量**: 3
- **最佳化合物ID**: CHEMBL1997924
- **最佳化合物SMILES**: `c1ccc(CNc2nc(Nc3cc(C4CC4)[nH]n3)c3sccc3n2)cc1`
- **活性类型**: Ki
- **活性值**: 1.0 nM

### 排名 17
- **靶标ID**: CHEMBL4225
- **靶标名称**: Dual specificity protein kinase CLK2
- **物种**: Homo sapiens
- **相似性打分**: 1.880000
- **相似性区间**: [1.486000, 1.880000]
- **平均相似性**: 1.612333
- **化合物数量**: 6
- **最佳化合物ID**: CHEMBL1997924
- **最佳化合物SMILES**: `c1ccc(CNc2nc(Nc3cc(C4CC4)[nH]n3)c3sccc3n2)cc1`
- **活性类型**: IC50
- **活性值**: 82.8 nM

### 排名 18
- **靶标ID**: CHEMBL4203
- **靶标名称**: Dual specificity protein kinase CLK4
- **物种**: Homo sapiens
- **相似性打分**: 1.880000
- **相似性区间**: [1.429000, 1.880000]
- **平均相似性**: 1.629000
- **化合物数量**: 11
- **最佳化合物ID**: CHEMBL1997924
- **最佳化合物SMILES**: `c1ccc(CNc2nc(Nc3cc(C4CC4)[nH]n3)c3sccc3n2)cc1`
- **活性类型**: IC50
- **活性值**: 51.3 nM

### 排名 19
- **靶标ID**: CHEMBL4852
- **靶标名称**: Mitogen-activated protein kinase kinase kinase kinase 5
- **物种**: Homo sapiens
- **相似性打分**: 1.880000
- **相似性区间**: [1.488000, 1.880000]
- **平均相似性**: 1.681333
- **化合物数量**: 3
- **最佳化合物ID**: CHEMBL1997924
- **最佳化合物SMILES**: `c1ccc(CNc2nc(Nc3cc(C4CC4)[nH]n3)c3sccc3n2)cc1`
- **活性类型**: Ki
- **活性值**: 100.0 nM

### 排名 20
- **靶标ID**: CHEMBL3788
- **靶标名称**: Serine/threonine-protein kinase PLK4
- **物种**: Homo sapiens
- **相似性打分**: 1.880000
- **相似性区间**: [1.492000, 1.880000]
- **平均相似性**: 1.772543
- **化合物数量**: 35
- **最佳化合物ID**: CHEMBL5175172
- **最佳化合物SMILES**: `Cc1cc(Nc2nc(NCc3ccc(C#N)cc3)nc3[nH]ncc23)n[nH]1`
- **活性类型**: IC50
- **活性值**: 10.5 nM

---

## 分析完成

**详细结果请查看**: `output.csv`

> 注：本报告基于相似性度量RefTverskyCombo方法和ChEMBL Version 35的化合物靶标数据分析而来。
