import csv
import sys

# Array to hold dictionaries for each row in the CSV
rows = []

# The filename is the first command line argument
filename = sys.argv[1]

# Open the file in read mode
with open(filename, 'r') as f:
    # Use csv's DictReader to create dictionaries for each row
    reader = csv.DictReader(f)
    
    for row in reader:
        rows.append(row)

# Now, rows is an array of dictionaries, each representing a transaction

# Initialize a variable to hold the total amount
total_amount_eur = 0

# Loop through each transaction, summing the "Amount (EUR)" field
for transaction in rows:
    # Convert the value to float
    amount = float(transaction["Amount (EUR)"])
    
    # If the amount is positive, add it to the total
    if amount > 0:
        total_amount_eur += amount

# Round the total amount to 2 decimal places
total_amount_eur = round(total_amount_eur, 2)

print(f"The total amount in EUR is {total_amount_eur}")
