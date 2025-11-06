
# ### Python : Mini Project - Orders Data Analysis



#read data from files
import pandas as pd
file_path ='/PATH/TO/ORDERS.CSV'
df = pd.read_csv(file_path)
df.head(20)


# handling NULL values
df['Ship Mode'].unique() #to check distinct values in dataframe


df = pd.read_csv(file_path,na_values=['Not Available','unknown'])
df['Ship Mode'].unique()


# rename column names and replace space with underscore
df.columns = df.columns.str.replace(' ','_')
df.columns = df.columns.str.lower()
df.columns


# derive new columns discount, sale_price and profit
df['discount'] = df['list_price']*df['discount_percent']*.01
df['sale_price'] = df['list_price'] - df['discount']
df['profit'] = df['sale_price'] - df['cost_price']
df.head(10)


# covert order_date from object data type to date
df['order_date'] = pd.to_datetime(df['order_date'],format='%Y-%m-%d')
df.dtypes


# drop cost_price, list_price and discount_percent columns
df.drop(columns = ['list_price','cost_price','discount_percent'], inplace = True)
df


import sqlalchemy as sal
engine = sal.create_engine('DATABASE_URL')
conn = engine.connect()


df.to_sql('df_orders', con=conn, index=False, if_exists = 'append' )

