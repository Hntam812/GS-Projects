import pandas as pd

import glob

from collections import Counter

from dev_functions import*

import warnings
warnings.filterwarnings('ignore')

db='key_metrics_raw'

def laz_biz(db,p,label):
    
    label='laz_biz'
    
    print('Pipeline : ' , label)
    
    print('')

    col_tmp=[]

    dataframe={}

    n=0

    print('### 1. Process files ')
    
    print('')
    
    for i in p:

        print('file : ', i)
        
        print('')
        
        a=pd.read_excel(i,header=0)
        
        date=a.columns[0].split(':')[-1].split('_')[-1]
        
        df=pd.read_excel(i, header=5)
        
        col=[col for col in df.columns]
        
        df['Date']=[date]*df.shape[0]
        
        state=compare_header_in_files(col_tmp,col)
        
        print('')
        
        if state==True:
            
            dataframe[n]=pd.concat([dataframe[n],df])
          
        else : 
           
            n+=1
           
            dataframe[n]=df
            
            warning(date,date)
            
            print('')
            
            col_tmp=col
    
    conclude(n)
    
    print('### 2. Pre-process dataframes and Storing to database.')
    
    print('')
    
    for key, df in dataframe.items():

        prepare_header_to_mysql(df)
        
        print('')
        
        df=df.sort_values('DATE').drop_duplicates()
        
        Date=store_data_to_local(db,df,label)
        
        print('')

        update_to_mysql(db,df,label,Date)
        
        print('')


def shp_biz(db,p,label):
    
    label='shp_biz'
    
    print('Pipeline : ' , label)
    
    print('')
    
    col_tmp=[]

    dataframe={}

    n=0
    
    print('### 1. Process files ')
    
    print('')
    
    for i in p:
        
        print('file : ', i)
        
        print('')
        
        df=pd.read_excel(i)
        
        col=[col for col in df.columns]
        
        date=i.split('/')[-1].split('_')[-1].split('.')[0]
        
        df['Date']=[date]*df.shape[0]
        
        df['Date']=[x[:4]+'-'+x[4:6]+'-'+x[6:] for x in df['Date'].tolist()]
        
        state=compare_header_in_files(col,col_tmp)
        
        print('')
        
        if state==True:
            
            dataframe[n]=pd.concat([dataframe[n],df])
            
        else : 
            
            n+=1
            
            dataframe[n]=df
            
            warning(date,date)
            
            print('')
            
            col_tmp=col

    conclude(5)
    
    print('')
    
    print('### 2. Pre-process dataframes and Storing to database.')
    
    print('')
        
    for key, df in dataframe.items():

        prepare_header_to_mysql(df)
        
        print('')
        
        df=df.sort_values('DATE').drop_duplicates()
        
        Date=store_data_to_local(db,df,label)
        
        print('')
        
        update_to_mysql(db,df,label,Date)
        
        print('')


def shp_overall(db,p,label):
    
    label='shp_overall'
    
    
    print('Pipeline : ' , label)
    
    print('')
    
    col_tmp=[]

    dataframe={}

    n=0
    
    print('### 1. Process files ')
    
    print('')
    
    for i in p:
        
        print('file : ', i)
        
        print('')
        
        df=pd.read_excel(i,sheet_name='Placed Order',dtype=str, skiprows=3)
        
        df['Date']=[x.split('-')[-1]+'-'+x.split('-')[1]+'-'+x.split('-')[0] for x in df['Date'].tolist()]
        
        date1=df['Date'].min()
        
        date2=df['Date'].max()
        
        col=[col for col in df.columns]
        
        state=compare_header_in_files(col,col_tmp)
        
        print('')
        
        if state==True:
            
            dataframe[n]=pd.concat([dataframe[n],df])
            
        else : 
            
            n+=1
            
            dataframe[n]=df

            warning(date1,date2)
            
            print('')
            
            col_tmp=col
    
    conclude(n)
    
    print('')
    
    print('### 2. Pre-process dataframes and Storing to database.')

    print('')

    for key, df in dataframe.items():
        
        prepare_header_to_mysql(df)
        
        print('')
        
        df=df.sort_values('DATE').drop_duplicates()
        
        Date=store_data_to_local(db,df,label)
        
        print('')

        update_to_mysql(db,df,label,Date)
        
        print('')


def tiki_seller_center(db,p,label):
    
    label='tiki_seller_center'
    
    
    print('Pipeline : ' , label)
    
    print('')

    col_tmp=[]

    dataframe={}

    n=0
    
    print('### 1. Process files ')
    
    print('')
    
    for i in p:
        
        print('file : ', i)
        
        print('')
        
        df=pd.read_excel(i,dtype=str)
        
        col=[col for col in df.columns]

        date=i.split('.')[-2]
        
        date=date[:4]+'-'+date[4:6]+'-'+date[6:]
        
        df['Date']=[date]*df.shape[0]
        
        date1=df['Date'].min()
        
        date2=df['Date'].max()
        
        state=compare_header_in_files(col,col_tmp)
        
        print('')
        
        if state==True:
            
            dataframe[n]=pd.concat([dataframe[n],df])
            
        else : 
            
            n+=1
            
            dataframe[n]=df

            warning(date1,date2)
            
            print('')
            
            col_tmp=col
        
    conclude(n)
    
    print('')
    
    print('### 2. Pre-process dataframes and Storing to database.')

    print('')
    
    for key, df in dataframe.items():
        
        unidecode_header(df)
        
        print('')
        
        prepare_header_to_mysql(df)
        
        print('')
        
        df=df.sort_values('DATE').drop_duplicates()
        
        Date=store_data_to_local(db,df,label)
        
        print('')

        update_to_mysql(db,df,label,Date)
        
        print('')

