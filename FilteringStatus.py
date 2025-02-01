import pandas as pd
import os

def count_unique_documents(dataframes, id_column='Document Title'):
    """Combine dataframes and count unique documents based on title"""
    combined_df = pd.concat(dataframes, ignore_index=True)
    return len(combined_df[id_column].unique())

def analyze_filtering_results():
    # Define directories and file patterns
    scopus_input_dir = "csv_output"
    scopus_output_dir = "filtered_output"
    ieee_input_dirs = [
        "What are the components of a dataproduct (non boolean)",
        "What are the components of microservice (boolean)",
        "What are the components of microservice (no boolean)"
    ]
    ieee_output_dir = "filtered_output_IEEE"

    # Initialize lists to store dataframes
    dp_before = []
    ms_before = []
    dp_after = []
    ms_after = []

    # Process Scopus files
    scopus_files = {
        "data_products": ["DataProduct_bool.csv", "DataProducts_nonbool.csv"],
        "microservices": ["Microservices_bool.csv", "Microservices_nonbool.csv"]
    }

    # Read Scopus original files
    for dp_file in scopus_files["data_products"]:
        file_path = os.path.join(scopus_input_dir, dp_file)
        if os.path.exists(file_path):
            dp_before.append(pd.read_csv(file_path))

    for ms_file in scopus_files["microservices"]:
        file_path = os.path.join(scopus_input_dir, ms_file)
        if os.path.exists(file_path):
            ms_before.append(pd.read_csv(file_path))

    # Read Scopus filtered files
    for dp_file in scopus_files["data_products"]:
        file_path = os.path.join(scopus_output_dir, f"filtered_{dp_file}")
        if os.path.exists(file_path):
            dp_after.append(pd.read_csv(file_path))

    for ms_file in scopus_files["microservices"]:
        file_path = os.path.join(scopus_output_dir, f"filtered_{ms_file}")
        if os.path.exists(file_path):
            ms_after.append(pd.read_csv(file_path))

    # Process IEEE files
    ieee_files = ["IEEE(Conference).csv", "IEEE(Books).csv", "IEEE(Journals).csv"]
    
    # Read IEEE original files
    for dir_path in ieee_input_dirs:
        for file_name in ieee_files:
            file_path = os.path.join(dir_path, file_name)
            if os.path.exists(file_path):
                df = pd.read_csv(file_path)
                if "dataproduct" in dir_path.lower():
                    dp_before.append(df)
                else:
                    ms_before.append(df)

    # Read IEEE filtered files
    for dir_path in ieee_input_dirs:
        for file_name in ieee_files:
            base_name = os.path.splitext(file_name)[0]
            file_path = os.path.join(ieee_output_dir, f"filtered_{base_name}_{dir_path}.csv")
            if os.path.exists(file_path):
                df = pd.read_csv(file_path)
                if "dataproduct" in dir_path.lower():
                    dp_after.append(df)
                else:
                    ms_after.append(df)

    # Calculate and display results
    print("\nDocument Count Analysis:")
    print("-" * 50)
    print("Data Products:")
    print(f"Before filtering: {count_unique_documents(dp_before)} unique documents")
    print(f"After filtering: {count_unique_documents(dp_after)} unique documents")
    print("\nMicroservices:")
    print(f"Before filtering: {count_unique_documents(ms_before)} unique documents")
    print(f"After filtering: {count_unique_documents(ms_after)} unique documents")

if __name__ == "__main__":
    analyze_filtering_results()