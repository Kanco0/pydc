Cafe Sales Data Cleaning Project
Date: 2026-01-14
Cleaned raw data of a cafe shop. Never knew what it contained, but I am goated fr. 🔥


First things first, I used two main libraries: Pandas and OS.
PANDAS: is the tool to clean the data.
OS : is used to locate the data file using 'abspath', since I put the data file in the same folder as py file.

First look:
I checked the rows and errors using 'isnull().sum()' to see how many unfilled cells were there.

The Cleaning Process:
Categorical Data: To be fast, I filled the missing text with the word 'unknown'. It is hard for me right now to decide their exact locations and I don't want to make mistakes, so by putting 'unknown' we prevent these columns from interfering with future analysis. We used 'df.fillna()' for 'Location', 'Payment Method', and 'Item'.

Numerical Data:
For 'Quantity' and 'Price Per Unit', I had to turn them into numerics using 'pd.to_numeric()' so pandas won't treat them as text.

Logic & Math:
I used the Mean(average) to fill the gaps in prices and quantities. This helps calculate the 'Total Spent' correctly. By using simple math "df['Quantity'] * df['Price Per Unit']", I granted a realistic price instead of just relying on the mean for the total.

Date: 
For the 'Transaction Date', I used 'ffill()'. What it does is look at the last transaction and copy its date to the next empty one. For example, if transaction 100 happened on the 12th, 101 is automatically at the same date. This avoids deleting this important column.
I sorted the dateset by 'Transaction ID' to make sure the dates follow a logical order, otherwise the fill would be messy.

Saving : 
I used df.to_csv() to save the work I just did