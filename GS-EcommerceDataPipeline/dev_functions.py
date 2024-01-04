### Functions process at local m

def compare_header_in_files(col_tmp,col):
    
    print('***** { Function } : compare_header_in_files() ')
    
    print('')
    
    from collections import Counter
    
    state=Counter(col_tmp)==Counter(col)
    
    if state==True:
        
        print('---> True ')

    else : 
        
        print('---> False ')
  
    return state


def compare_header_dataframe_to_table(l1,l2):
    
    print('***** { Function } : compare_header_dataframe_to_table() ')
    
    print('')
    
    from collections import Counter
    
    state=Counter(l1)==Counter(l2)
    
    if state==True:
        
        print('---> True ')
        
        
    else : 
        
        print('---> False ')
        
    return state


def unidecode_header(df):
    
    print('***** { Function } : unidecode_header() ')
    
    print('')

    from unidecode import unidecode

    df.rename(columns={col: unidecode(col) for col in df.columns}, inplace=True)
    
    return df

     
def prepare_header_to_mysql(df):
    
    print('***** { Function } : prepare_header_to_mysql() ')
    
    print('')
    
    import re

    new_header = [re.sub('[^0-9a-zA-Z_]+', '_', col) for col in df.columns]

    new_header = [col[:64] for col in new_header]

    new_header = [col if col[0].isalpha() else "col_" + col for col in new_header]

    df.columns = new_header
    
    df=unidecode_header(df)
    
    df.columns=[x.upper() for x in df.columns]

    df.columns=[x[:-1] if x.endswith("_") else x for x in df.columns]
    
    return df


def store_data_to_local(db,df,label):
    
    print('***** { Function } : store_data_to_local() ')
    
    print('')    
            
    Date=df['DATE'].min()

    Date=Date.replace('-','')
    
    Date=Date[:8]
    
    db=db.replace('db','_').replace('_raw','/')
        
    output='data/output_' +db+ label +'_'+ Date+ '.xlsx'
        
    print('---> local : ',output)
    
    print('')  
    
    head=df.head()
    
    print('dataframe-head : \n', head)
    
    print('') 
    
    tail=df.tail()
    
    print('dataframe-tail : \n', tail)
    
    print('') 
       
    df.to_excel(output,index=False)
    
    return Date


def warning(date1,date2):

    print('*'*50)
    
    print('')
    
    print (' ===> Warning : file changes header-columns name !')
    
    print('')
    
    print (' Date : ',date1+' - ',date2)
    
    print('')
          
    print('*'*50)


def conclude(n):
    
    print(' _ '*30)
    
    print('')
    
    print('===> total :  ', str(n) + ' dataframes.')
    
    print('')
    
    print('________________________________________________________________________________________________________________________________________________________________________')
    
    print('')


def get_table_name_latest_in_record(db,query):
    
    print('***** { Function } :  get_table_name_latest_in_record(query): ')
    
    print('')    
    
    import pymysql

    # Establish a connection to the MySQL database
    connection = pymysql.connect(host='localhost',
                                user='t',
                                password='a',
                                db=db)

    # Create a cursor object

    cursor = connection.cursor()

    # Execute a query

    #query='SELECT table_name FROM record WHERE id = (SELECT max(id) FROM record WHERE label = "' + label + '" )'
    
    print('---> execute query : ', query)
    
    print('')

    # value = 'your_value'

    cursor.execute(query)

    # Fetch the results

    results = cursor.fetchone()

    # Print the results
    
    table_name=results[0]

    print('---> table name latest : ', table_name)
    
    print('')

    # Close the cursor and the database connection

    cursor.close()

    connection.close()
    
    return table_name
    

def get_header_from_table_in_mysql(db,query):
    
    print('***** { Function } :  get_header_from_table_in_mysql() ')
    
    print('')

    import pymysql

    # Establish a connection to the MySQL database
    
    connection = pymysql.connect(host='localhost',
                                user='t',
                                password='a',
                                db=db)

    # Create a cursor object

    cursor = connection.cursor()

    # Execute a query

    # query = "SHOW COLUMNS FROM table_name"
    
    print('---> execute query : ', query)
    
    print('')

    # value = 'your_value'

    cursor.execute(query)

    # Fetch the results

    results = cursor.fetchall()

    l1=[]

    # Print the results

    for row in results:
        
        l1.append(row[0])

    print('---> header of table in mysql : ',l1)
    
    print('')

    # Close the cursor and the database connection

    cursor.close()

    connection.close()
    
    return l1


def store_data_to_mysql(db,df,table_name):

    print('***** { Function } : store_data_to_mysql() ')
    
    print('')  
    
    from sqlalchemy import create_engine
    
    # Create SQLAlchemy engine to connect to MySQL Database

    hostname="localhost"
    dbname=db     
    uname="t"                                   
    pwd="a"

    engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
                        .format(host=hostname, db=dbname, user=uname, pw=pwd))

    # store dataframe to mysql 
    
    df.to_sql(table_name, engine, index=False,if_exists='append')
    
    print('---> stored data to mysql successful, table name : ', table_name )
    
    print('')  


def update_table_name_to_record(db,table_name_new,label):
    
    print('***** { Function } : update_table_name_to_record() ')
    
    print('')  
    
    import pandas as pd
    
    import pymysql

    # Establish a connection to the MySQL database
    connection = pymysql.connect(host='localhost',
                                user='t',
                                password='a',
                                db=db)

    # Create a cursor object

    cursor = connection.cursor()

    # Execute a query

    import datetime
 
    current_time = datetime.datetime.now()
    
    current_time=str(current_time)
    
    current_time=current_time[:16]

    query="INSERT INTO record(table_name, label , date_time) VALUES "+ "( '" + table_name_new + "' , '" + label + "' , '" + current_time + "' );"
    
    print('---> execute query : ', query)
    
    print('')
    # value = 'your_value'

    cursor.execute(query)

    connection.commit()

    # Define the SQL query to read data from the table
    query = "SELECT * FROM record"
    
    print('---> execute query : ', query)
    
    print('')

    # Execute the read query and fetch the results
    cursor.execute(query)
    
    results = cursor.fetchall()

    # Create a Pandas dataframe from the query results
    df = pd.DataFrame(results, columns=[desc[0] for desc in cursor.description])

    print('---> record : ')
    
    print('')

    # Close the database connection and return the dataframe
    connection.close()
    
    return print(df)
    

def update_to_mysql(db,df,label,Date):
    
    print('***** { Function } : update_to_mysql() ')
    
    print('')

    query='SELECT table_name FROM record WHERE id = (SELECT max(id) FROM record WHERE label = "' + label + '" )'

    table_name=get_table_name_latest_in_record(db,query)
    
    print('')

    query='SHOW COLUMNS FROM ' + table_name  

    l1=get_header_from_table_in_mysql(db,query)
    
    print('')
           
    l2=[col for col in df.columns] 
    
    print('---> header of table in external : ',l2)
    
    print('')

    status=compare_header_dataframe_to_table(l1,l2)
    
    print('')

    if status == True:        
            
        store_data_to_mysql(db,df,table_name)
        
        print('')
        
    else:
           
        table_name_new=label+'_'+Date
                        
        update_table_name_to_record(db,table_name_new,label)
        
        print('') 

        store_data_to_mysql(db,df,table_name_new)
        
        print('')
        
