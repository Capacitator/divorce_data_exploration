import pandas as pd

# Set display options for pandas
pd.set_option('display.max_columns', 11)
pd.set_option('display.width', 500)

# Load data from Stata files using chunksize to read in smaller portions
df_cases = pd.read_stata("dummy_location/cases_2018.dta", chunksize=10000)
df_purpose = pd.read_stata("dummy_location/purpose_name_key.dta", chunksize=10000)
df_type = pd.read_stata("dummy_location/type_name_key.dta", chunksize=10000)
df_acts = pd.read_stata("dummy_location/acts_sections.dta", chunksize=10000)

# Read only a specific number of rows from each DataFrame
df_cases = df_cases.read(nrows=30000000)
df_purpose = df_purpose.read(nrows=500)
df_type = df_type.read(nrows=5000000)
df_acts = df_acts.read(nrows=500)

# Drop unnecessary columns from df_cases DataFrame
df_cases = df_cases.drop(['ddl_case_id', 'cino', 'judge_position', 'date_of_filing', 'date_of_decision', 'date_first_list', 'date_last_list', 'date_next_list'], axis=1)

# Define the type names to filter
type_names_to_show = [
    3933, 3936, 3942, 3952, 3981,
    3985, 3986, 3991, 3994, 5277,
    2431, 3925, 3928, 3968, 3972,
    3973, 3980, 5306
]

# Filter df_cases to include only the specified type names
filtered_df_cases = df_cases[df_cases['type_name'].isin(type_names_to_show)]

# Print the filtered DataFrame
print(filtered_df_cases)

'''
filtered_df_type = df_type[df_type['type_name_s'].isin([
    'maint. case',
    'maintainance 488',
    'maintanance case 125 cr.pc',
    'maintenance 488',
    'mat (gaurdian and wards)',
    'mat (r and c)',
    'mat (r&c)',
    'mat ex',
    'mat exe.',
    'pet u/s 75 of christian marriage and divorce act',
    'divorce on mutul consent',
    'petition u/s 98 christian marriage and divorce act'
])]
'''
# Print the filtered DataFrame
#print(filtered_df_type.to_string(index=False))
#unique_type_names = df_type['type_name_s'].unique()
#for name in unique_type_names:
#    print(name)
#print(df_acts)
# Merge the DataFrames on 'type_name' and 'year' columns
#merged_df = pd.merge(df_cases, df_type, on=['type_name', 'year'], how='right')
#merged_df = merged_df.drop(['ddl_case_id', 'cino','judge_position','date_of_filing',  'date_of_decision',  'date_first_list',  'date_last_list',  'date_next_list'], axis=1)
#print(merged_df[merged_df['purpose_name'].notnull()])
# Now, merged_df will contain 'Case type', 'type_name_key', and other columns from both DataFrames
# You can select the columns you need
#result = merged_df[['Case type', 'type_name_key']]
#print(result)
##print(df.columns.tolist())
###
