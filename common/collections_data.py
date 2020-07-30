# Import the python CSV module
import csv

entries = []
# Create a python file object in read mode for the baby_names.csv file: csvfile
with open('cta_daily_station_totals.csv', 'r') as csvfile : 
    # Loop over a csv reader on the file object
    for row in csv.reader(csvfile):
        # Add list to entries
        entries.append(tuple(row))
    
entries.pop(0)