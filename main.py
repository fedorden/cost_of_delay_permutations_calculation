import pandas as pd
import itertools


permutations = list(itertools.permutations([1, 2, 3, 4, 5, 6, 7, 8]))

input_df = pd.read_csv ('input.csv')

column_names = ["Priorities list", "Total CoD"]
output_df = pd.DataFrame(columns = column_names)

for permutation in permutations:
    time_in_queue = 0
    total_cod = 0
    for item in permutation:
        row = input_df.loc[input_df['#'] == item]
        item_dev_estimation = row.at[item-1, 'Preliminary development estimation (weeks)']
        item_cod_week = row.at[item-1, 'Total CoD week']

        time_in_queue = time_in_queue + item_dev_estimation
        item_cod = item_cod_week * time_in_queue
        total_cod = total_cod + int(item_cod)

    output_df = output_df.append({
        "Priorities list" : permutation,
        "Total CoD": total_cod
    },ignore_index=True)
        
output_df.to_csv('output.csv')
sorted_output = output_df.sort_values(by='Total CoD',ascending=True)
print(sorted_output.head(10))
sorted_output.head(10).to_csv('short_output.csv')
