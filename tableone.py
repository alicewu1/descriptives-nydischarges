import pandas as pd 
from tableone import TableOne, load_dataset ## Receiving ImportError: tableone cannot be imported from partially initialized module 'tableone' (most likely due to a circular import)

sparcs=pd.read_csv('https://health.data.ny.gov/resource/gnzp-ekau.csv') # used csv link from API
sparcs
sparcs.dtypes
sparcs_columns = ['gender', 'length_of_stay', 'total_costs']
sparcs_categorical = ['gender', 'length_of_stay']
sparcs_groupby = ['length_of_stay']
sparcs_labels={'total_costs': 'final_costs'}

sparcsTab1 = TableOne(sparcs, columns=sparcs_columns, categorical=sparcs_categorical, groupby=sparcs_groupby, rename=sparcs_labels, pval=False )
## still receiving a 'TableOne' is not defined error due to import error
## used Google Colab to resolve errors

print(sparcsTab1.to_csv('data/tableone_test.csv'))
