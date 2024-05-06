import pandas as pd

sales_df = pd.read_csv('data/daily_sales.csv')

sales_df['date'] = sales_df['date'].apply(lambda x: str(x)[:10])
sales_df['sku'] = sales_df['sku'].astype('str')