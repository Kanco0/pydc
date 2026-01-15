# %%
import pandas as pd
import os 
import re

c_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(c_dir, 'dirty_cafe_sales.csv')
df = pd.read_csv(file_path)
df = df.fillna({
    "Location": "Unknown",
    "Payment Method": "Unknown",
    "Item": "Unknown"
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

def clean_text(text):
    if not isinstance(text, str):
        return ""
    text = re.sub(r'(.)\1+', r'\1\1', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text
df['Item'] = df['Item'].apply(clean_text)
df['Location'] = df['Location'].apply(clean_text)


df['Price Per Unit'] = df['Price Per Unit'].round(2)
df['Total Spent'] = df['Total Spent'].round(2)
df['Quantity'] = df['Quantity'].round(2)
df = df.reset_index(drop=True)

garbage_values = ['ERROR', 'UNKNOWN', 'Unkown', 'unregistered', 'Registered']

df['Item'] = df['Item'].replace(garbage_values, 'Unknown')

df['Location'] = df['Location'].replace(garbage_values, 'Unknown')
df['Payment Method'] = df['Payment Method'].replace(garbage_values, 'Unknown')

unique_items = df['Item'].unique()

global_fixes = {
    'ERROR': 'Unknown',
    'UNKNOWN': 'Unknown',
}
target_cols = ['Location', 'Payment Method', 'Item']
df[target_cols] = df[target_cols].replace(global_fixes)
print(df)
print("---list columns----")
print("---check data---")
print(df.head())
print(list(df.columns))
print("----erros----")
print(df.isnull().sum())
print("---duplicates---")
print(f"Total Duplicates: {df.duplicated().sum()}")
print("--- Unique Items Found ---")
print(df['Item'].unique())
print("--- قائمة الأصناف الموجودة في عمود Item ---")
for item in sorted(unique_items):
    print(item)
df.to_csv('cleaned_cafe_sales_data.csv', index=False)