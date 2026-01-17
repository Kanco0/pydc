<h1 aling="center">2026-01-14</h1>

<h2>📌 Project Summary: Cafe Sales Data Cleaning</h2>

The Problem: The raw dataset from a cafe shop was messy and inconsistent, with missing values in Location, Payment Method, Item, Quantity, Price Per Unit, and Transaction Date. Extra spaces, inconsistent text formats, and minor errors made it unusable for analysis or reporting.

The Fix: I cleaned the data using Python and Pandas by:

Filling missing text fields (Location, Payment Method, Item) with “Unknown”

Converting numeric columns (Quantity, Price Per Unit) and calculating Total Spent

Filling missing Transaction Dates logically using forward-fill after sorting by Transaction ID

Removing extra spaces, standardizing text case, and fixing duplicates in string columns

Rounding numeric columns to 2 decimal places for consistency and efficiency

The Result: A fully cleaned, analysis-ready dataset that allows the cafe to track sales, inventory, and revenue accurately. The dataset is structured, consistent, and ready for further business analysis or reporting.

📁 Repository contains:

raw_data/ → Original messy CSV file

cleaned_data/ → Cleaned and standardized CSV

scripts/ → Python scripts used for cleaning

Before/After examples for quick reference
<hr>

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

<h3 align="center">-------------------------------</h3>

-DATE: 2026-01-15

cleaning extra space :

for it I had to check if the cell it self contains a string not a number, by using isinstance().

and for cleaning extra spaces the \s+ means look for any empty space even if its on or 10 or a new line and delete it. the + means 1 or more.

the re.sub tells py whenever you find a lot of empty space change it with 1 space only.

Finnaly .strip() comes in the end as it cleans and delete any space in the start or the end of the text.

final touches :
After I used the library of TextBlob it appeared its kinda stupid in a look a like situation 
in the first place, I don't even need it. because after I used  
'for item in sorted(unique_items):
    print(item)'
this made sense because there is not spelling mistakes but there is another mistakes such as duplicates and lower cases I could see this as UNKNOWN and Unknown appeared twice, the system is so sensitive to lower and upper cases.
by that I just did what every one have to do if they have such a simple machine from data, and is it to use global.replace
for its we know that we have 2 same purpose words wich are (ERROR, UNKNOWN)
using it with only the string colunms well grant to make next data analysis affictive. 

also I added for the values such as Price per unit, Total Spent, Quantity [.round2] for it well make it consume less token in the future.

Saving : 

I used df.to_csv() to save the work I just did

<br>
<hr>
<br>
<h2 align="center">DIRTY DATA</h2>
<p align="center">
  <img src="https://raw.githubusercontent.com/Kanco0/pydc/main/dc1/dirtydata.png" width="60%">
</p>

<h2 align="center">CLEANED DATA</h2>
<p align="center">
  <img src="https://raw.githubusercontent.com/Kanco0/pydc/main/dc1/cleaneddata.png" width="60%">
</p>



