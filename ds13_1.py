# %%
import pandas as pd
import os 
c_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(c_dir, 'dirty_cafe_sales.csv')
df = pd.read_csv(file_path)
df = df.fillna({
    "Location": "Unkown",
    "Payment Method": "Unkown",
    "Item": "Unregistered"
    })
df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
df['Price Per Unit'] = pd.to_numeric(df['Price Per Unit'], errors='coerce')
df['Transaction Date'] = pd.to_datetime(df['Transaction Date'], errors='coerce')


mean_qty = df['Quantity'].mean()
mean_price = df['Price Per Unit'].mean()
df = df.sort_values('Transaction ID')

df['Quantity'] = df['Quantity'].fillna(mean_qty)
df['Price Per Unit'] = df['Price Per Unit'].fillna(mean_price)
df['Transaction Date'] = df['Transaction Date'].ffill()

df['Total Spent'] = df['Price Per Unit'] * df['Quantity']

print(df)
print("---list columns----")
print(list(df.columns))
print("----erros----")
print(df.isnull().sum())
df.to_csv('cleaned_cafe_sales_data.csv', index=False)
# %%
