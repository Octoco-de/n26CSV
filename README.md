# N26CSV

This is a simple script to grab the CSV exported by N26 and calculate the sum of incoming values (positive transactions only). 

The script is written in Python and uses the built-in `csv` and `sys` modules. It reads the CSV file line by line and treats each line as a dictionary object. The "Amount (EUR)" value of each transaction is added to a running total if it is a positive value. The final sum is rounded to two decimal places and printed out.

## Requirements

- Python 3.6 or higher

## How to Run

To run the script, you'll need to pass the filename as a command line argument. 

1. Open a Terminal window.

2. Navigate to the directory containing the script and your CSV file.

3. Run the following command:

   ```bash
   python3 N26-CSV.py yourfilename.csv
