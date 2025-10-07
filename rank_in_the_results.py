import pandas as pd

# 假设 df 是你的 DataFrame
# 首先按 'RefTverskyCombo' 列从高到低排序
df_sorted = df.sort_values(by='RefTverskyCombo', ascending=False)

# 计算排名，并将排名结果添加到原 DataFrame 的新列 'rank' 中
# 使用 method='min'
df['rank_min'] = df['RefTverskyCombo'].rank(method='min', ascending=False)
# 或者使用 method='dense'
df['rank_dense'] = df['RefTverskyCombo'].rank(method='dense', ascending=False)

# 现在查找 name 为 'CHEMBL1997924' 的行的排名
target_name = 'CHEMBL1997924'
# 使用 .loc 进行布尔索引，并获取排名列的值
rank_value_min = df.loc[df['name'] == target_name, 'rank_min'].iloc[0]
rank_value_dense = df.loc[df['name'] == target_name, 'rank_dense'].iloc[0]

print(f"基于 'min' 方法, name 为 '{target_name}' 的排名是: {rank_value_min}")
print(f"基于 'dense' 方法, name 为 '{target_name}' 的排名是: {rank_value_dense}")

# 如果你想直接看排序后的表中这个name排在第几行（行索引，从0开始计数）
# 这通常不是“排名”，但有时也被询问
position_in_sorted_index = df_sorted.index[df_sorted['name'] == target_name].tolist()[0]
print(f"在排序后的表格中，name 为 '{target_name}' 的行索引位置是: {position_in_sorted_index}")
