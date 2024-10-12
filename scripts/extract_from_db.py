import pandas as pd
import sqlalchemy as sal

# Criando a conecção com o Banco de dados do SQL Server
engine = sal.create_engine(r'mssql://PC-Gabriel\SQLEXPRESS/etL_python_sql?driver=ODBC+DRIVER+17+FOR+SQL+SERVER',
                           isolation_level="AUTOCOMMIT")
conn = engine.connect()

# Montando a query
query = """
    SELECT TOP (1000) [order_id]
      ,[order_date]
      ,[ship_mode]
      ,[segment]
      ,[country]
      ,[city]
      ,[state]
      ,[postal_code]
      ,[region]
      ,[category]
      ,[sub_category]
      ,[product_id]
      ,[quantity]
      ,[discount]
      ,[sale_price]
      ,[total_profit]
  FROM [etl_python_sql].[dbo].[df_orders];
"""

# Lendo os dados da query e trazendo para um DF do pandas
df = pd.read_sql(query, conn)
conn.close()

# Salvando os dados do DF em um arquivo CSV
path = r'data/processed/orders_processed.csv'
df.to_csv(path, index=False)