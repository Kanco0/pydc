Cafe Sales Data Cleaning Project
-DATE: 2026-01-14

Cleaned raw data of a cafe shop. Never knew what it contained. was so good to learn on it how to data clean.

First things first, I used two main libraries: Pandas and OS.
Pandas is the main tool used to clean and manipulate the data.
OS is used to locate the data file using abspath, since the CSV file is in the same folder as the Python file.

First look:

I checked missing values and errors using isnull().sum() to see how many unfilled cells were present in each column.

The Cleaning Process:

To keep the process fast and safe, I filled missing text values with the word "Unknown". At this stage, it was difficult to determine the correct values without risking mistakes, so using "Unknown" prevents these columns from interfering with future analysis.
I used df.fillna() for the Location, Payment Method, and Item columns.

Numerical Data:

For Quantity and Price Per Unit, I converted the columns to numeric values using pd.to_numeric(), so Pandas would not treat them as text.

Logic & Math:

I used the mean (average) to fill missing values in Quantity and Price Per Unit. This helps ensure that Total Spent is calculated correctly.
By calculating Quantity * Price Per Unit, I generated a realistic total instead of filling the total column directly with averages.

missing Date : 

For Transaction Date, I used ffill(). This method copies the previous valid date into the next missing row. For example, if transaction 100 happened on the 12th, transaction 101 is assumed to be on the same date.
I sorted the dataset by Transaction ID before applying this method to ensure the dates follow a logical order.

------------------------------------------------------------------------------------------
-DATE: 2026-01-15

cleaning extra space :

for it I had to check if the cell it self contains a string not a number, by using isinstance().

and for cleaning extra spaces the \s+ means look for any empty space even if its on or 10 or a new line and delete it. the + means 1 or more.

the re.sub tells py whenever you find a lot of empty space change it with 1 space only.

Finnaly .strip() comes in the end as it cleans and delete any space in the start or the end of the text.

Misspelling correction:

First, I used the TextBlob library with from textblob import TextBlob, as it is a really effective and fast way to handle spelling correction.
I used unique() to reduce repeated processing and improve performance.
Using correction_map, I created an empty dictionary.

The loop and if statement are used because TextBlob sometimes changes business spellings into standard English words; by using this logic, I protected the data from unwanted changes.

For TextBlob role, I applied it only to words that were not on the protection list, such as coffee or salad, so they go to the else condition. There, TextBlob compares the word to the English dictionary and auto-corrects it.

For the last step, I used .map(). Instead of processing the data line by line, I applied the correction map (dictionary) directly to the Item column.

global fix:

Merging variations such as "ERROR", "Unknown", and "UNKNOWN". All of them represent missing values but with different names. By converting them all to "Unknown", I merged these variations, which makes later analysis more accurate and consistent.

Correction of business logic: the word "Take" may be grammatically correct, but in cafe systems the correct term used is "Takeaway". This change ensures that the Location and Item columns stay safe from TextBlob over-correction.

'df.replace(global_fixes)' is used to scan the entire CSV across all columns and rows. If an identical value is found, it is replaced with the mapped value. This approach is faster and cleaner than using multiple if/else conditions.

Saving : 
I used df.to_csv() to save the work I just did