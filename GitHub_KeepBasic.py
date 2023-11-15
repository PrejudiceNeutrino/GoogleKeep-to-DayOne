'''

This code converts Google Keep notes into a .csv that can be imported into DayOne via iOS.
All you have to do is set the file paths to where you have the JSON files and where you want the output CSV to end up.

'''

import os
import json
import csv
from datetime import datetime

# Function to convert UNIX timestamp to a readable date and time
def convert_unix_timestamp(timestamp_usec):
    # Convert UNIX timestamp to seconds
    timestamp_sec = timestamp_usec / 1_000_000
    # Format the timestamp as a string in UTC time
    return datetime.utcfromtimestamp(timestamp_sec).strftime('%Y-%m-%dT%H:%M:%S.000Z')

# Directory containing your JSON files
json_dir = r'C:\Users\DayOne\Google Keep to DayOne\KeepNotes'

# Output CSV file
csv_file = r'C:\Users\DayOne\Google Keep to DayOne\output.csv'

# List to store data
data = []

# Loop through each JSON file in the directory
for filename in os.listdir(json_dir):
    if filename.endswith('.json'):
        with open(os.path.join(json_dir, filename), 'r', encoding='utf-8') as file:
            # Load JSON data
            json_data = json.load(file)

            # Extract relevant information
            created_timestamp_usec = json_data.get('createdTimestampUsec', 0)
            text = json_data.get('textContent', '')

            # Convert UNIX timestamp to readable format
            created_datetime = convert_unix_timestamp(created_timestamp_usec)

            # Append data to the list
            data.append([created_datetime, text])

# Write data to CSV file
with open(csv_file, 'w', encoding='utf-8', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    
    # Write header
    csv_writer.writerow(['date', 'text'])

    # Write data
    csv_writer.writerows(data)

# Print a completion message
print(f"Conversion completed. Data written to {csv_file}")