import csv
from pybtex.database import parse_file, BibliographyData
import sys
from datetime import datetime
import os

def log_error(error_file, bib_file, entry_key, error_msg):
    with open(error_file, 'a', encoding='utf-8') as f:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        f.write(f"{timestamp} - File: {bib_file} - Entry: {entry_key} - Error: {error_msg}\n")

def convert_bib_to_csv(bib_file, input_dir, output_dir):
    # Define CSV headers
    fieldnames = ['key', 'title', 'authors', 'year', 'journal', 'abstract', 'doi']
    
    # Create output filename from input filename
    input_path = os.path.join(input_dir, input_file)
    base_name = os.path.splitext(os.path.basename(bib_file))[0]
    output_file = os.path.join(output_dir, f"{base_name}.csv")
    error_file = os.path.join(output_dir, "conversion_errors.log")
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Open output CSV file
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        try:
            print(f"Processing file: {input_path}")
            bib_data = parse_file(input_path)
            
            # Process each entry
            for entry_key, entry in bib_data.entries.items():
                try:
                    # Extract authors
                    authors = '; '.join(str(author) for author in entry.persons.get('author', []))
                    
                    # Create row dictionary
                    row = {
                        'key': entry_key,
                        'title': entry.fields.get('title', ''),
                        'authors': authors,
                        'year': entry.fields.get('year', ''),
                        'journal': entry.fields.get('journal', ''),
                        'abstract': entry.fields.get('abstract', ''),
                        'doi': entry.fields.get('doi', '')
                    }
                    
                    writer.writerow(row)
                    
                except KeyError as e:
                    error_msg = f"Missing required field: {e}"
                    log_error(error_file, bib_file, entry_key, error_msg)
                    print(f"Error processing entry {entry_key}: {error_msg}")
                    continue
                    
        except Exception as e:
            error_msg = str(e)
            log_error(error_file, bib_file, "FILE_LEVEL", error_msg)
            print(f"Error processing file {bib_file}: {error_msg}")

if __name__ == "__main__":
    input_dir = "ACM_bib"

    input_files = ["DataProduct_bool.bib", "DataProducts_nonbool.bib", 
                   "Microservices_bool.bib", "Microservices_nonbool.bib"]
    output_dir = "csv_output"
    
    for input_file in input_files:
        convert_bib_to_csv(input_file, input_dir ,output_dir)