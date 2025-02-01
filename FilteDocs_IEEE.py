# Imports
import pandas as pd
import os

# Define input files and output directory
input_dir = ["What are the components of a dataproduct (non boolean)", "What are the components of microservice (boolean)", "What are the components of microservice (no boolean)"]
output_dir = "filtered_output_IEEE"
input_files = ["IEEE(Conference).csv", "IEEE(Books).csv", 
               "IEEE(Journals).csv"]


# Define keywords for filtering
data_product_keywords = [
    'data product',
    'data products',
    'data as a product',
    'data mesh'
]

microservice_keywords = [
    'microservice',
    'microservices',
    'micro-service',
    'micro-services',
    'service oriented'
]

microservice_definition_keywords = [
    'defin',  # catches 'define', 'defining', 'definition'
    'character',  # catches 'characteristic', 'characteristics'
    'component',
    'architecture',
    'requirement',
    'essential',
    'fundamental'
]
def check_abstract(abstract):
    if not isinstance(abstract, str):
        return False
    
    abstract = abstract.lower()
    has_data_product = any(keyword in abstract for keyword in data_product_keywords)
    has_microservice = any(keyword in abstract for keyword in microservice_keywords)
    
    # If it's a microservice paper, check for definition-related keywords
    if has_microservice:
        has_definition = any(keyword in abstract for keyword in microservice_definition_keywords)
        return has_definition
    
    return has_data_product  # Return true for data product papers regardless

def filter_and_display(input_file, input_dirs, output_dir):
    for input_dir in input_dirs:
        # Create full input and output paths
        input_path = os.path.join(input_dir, input_file)
        
        # Skip if file doesn't exist
        if not os.path.exists(input_path):
            print(f"Skipping - File not found: {input_path}")
            continue
            
        base_name = os.path.splitext(os.path.basename(input_file))[0]
        output_file = os.path.join(output_dir, f"filtered_{base_name}_{input_dir}.csv")
        
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Read and filter DataFrame
        df = pd.read_csv(input_path)
        filtered_df = df[df['Abstract'].apply(check_abstract)]

        # Display results
        print(f"\nProcessing file: {input_path}")
        print(f"Original number of papers: {len(df)}")
        print(f"Filtered number of papers: {len(filtered_df)}")

        # Save filtered results
        filtered_df.to_csv(output_file, index=False)
        print(f"Saved filtered results to: {output_file}")

if __name__ == "__main__":
    for input_file in input_files:
        filter_and_display(input_file, input_dir, output_dir)