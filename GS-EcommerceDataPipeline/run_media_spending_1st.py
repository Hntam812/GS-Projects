
import glob 

import pandas as pd

from dev_functions import*

p='data_sample.xlsx'

df=pd.read_excel(p)

db='media_spending_raw'

print('---> store a sample data to mysql : ')

print('')

print(df)

print('')

label=[ 'laz_aff' , 'laz_search' , 'shp_aff' , 'shp_search', 'tiki_aff' , 'tiki_search'  ]

for label in label : 
    
    update_table_name_to_record(db,label,label)
    
    print('')
    
    store_data_to_mysql(db,df,label)
    
    print('')
    
