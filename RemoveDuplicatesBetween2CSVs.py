'''
The purpose of this is to compare 2 .csv files and delete duplicate text entries.
I made this to compare Google Keep and iCloud notes and then import them into DayOne.
'''

import csv
from fuzzywuzzy import fuzz

def remove_duplicate_entries(input_file1, input_file2, output_file, threshold=90):
    # Read data from the first CSV file
    with open(input_file1, 'r', newline='', encoding='utf-8') as csvfile1:
        reader1 = csv.DictReader(csvfile1)
        data1 = list(reader1)

    # Read data from the second CSV file
    with open(input_file2, 'r', newline='', encoding='utf-8') as csvfile2:
        reader2 = csv.DictReader(csvfile2)
        data2 = list(reader2)

    unique_entries = [data1[0]]  # Keep the header as the first entry

    # Loop through entries in the first CSV file
    for entry1 in data1[1:]:
        text_to_compare = entry1['text']

        # Check if there is similar text in data2 based on the specified threshold
        duplicate_texts = [entry2 for entry2 in data2 if fuzz.ratio(text_to_compare, entry2['text']) >= threshold]

        # If no duplicates found, add the entry to the list of unique entries
        if not duplicate_texts:
            unique_entries.append(entry1)

    # Write the unique entries to the output CSV file
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['date', 'text']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for entry in unique_entries[1:]:
            if entry['text']:  # Exclude entries with empty text
                writer.writerow(entry)


if __name__ == "__main__":
    # Specify the paths for input and output CSV files
    input_csv1 = r'C:\Users\DayOne\Google Keep to DayOne\Keep_Output.csv'
    input_csv2 = r'C:\Users\DayOne\iOS to DayOne\IOS_Output.csv'
    output_csv = r'C:\Users\Google Keep to DayOne\RemovedDuplicates.csv'

    # Call the function to remove duplicate entries
    remove_duplicate_entries(input_csv1, input_csv2, output_csv)
