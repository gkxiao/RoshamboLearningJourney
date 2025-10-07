import pandas as pd

# Read the scoring results into a DataFrame
df = pd.read_csv('chembl35_conf25_hits_score.csv')

# Basic descriptive statistics for key scoring metrics
stats = df.describe()
combo_score_stats = stats[['tanimoto_combo_legacy', 'tanimoto_combination', 'RefTverskyCombo', 'FitTverskyCombo']]
print('Descriptive statistics for key combination scores')
print(combo_score_stats)

# First, sort the DataFrame by 'RefTverskyCombo' column in descending order (highest to lowest)
df_sorted = df.sort_values(by='RefTverskyCombo', ascending=False)

# Calculate rankings and add them as new columns to the original DataFrame
# Using method='min' (standard competition ranking: 1, 2, 2, 4)
df['rank_min'] = df['RefTverskyCombo'].rank(method='min', ascending=False)
# Using method='dense' (dense ranking: 1, 2, 2, 3)
df['rank_dense'] = df['RefTverskyCombo'].rank(method='dense', ascending=False)

# Now find the rank of the row where 'name' equals 'CHEMBL1997924'
target_name = 'CHEMBL1997924'
# Use .loc with boolean indexing to get the rank values
rank_value_min = df.loc[df['name'] == target_name, 'rank_min'].iloc[0]
rank_value_dense = df.loc[df['name'] == target_name, 'rank_dense'].iloc[0]

print(f"Using 'min' ranking method, the rank for name '{target_name}' is: {rank_value_min}")
print(f"Using 'dense' ranking method, the rank for name '{target_name}' is: {rank_value_dense}")

# If you want to see the actual position (row index, starting from 0) of this name in the sorted table
# This is typically not considered a "rank" but is sometimes requested
position_in_sorted_index = df_sorted.index[df_sorted['name'] == target_name].tolist()[0]
print(f"In the sorted DataFrame, the row index position for name '{target_name}' is: {position_in_sorted_index}")
