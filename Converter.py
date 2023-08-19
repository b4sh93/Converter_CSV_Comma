import pandas as pd

def convert_delimiter(input_filepath, output_filepath):
    """
    Convert the delimiter of a CSV file from semicolon to comma.
    
    Parameters:
    - input_filepath: Path to the input CSV file with semicolon delimiter.
    - output_filepath: Path to save the output CSV file with comma delimiter.
    """
    # Read the CSV file using semicolon as the delimiter
    df = pd.read_csv(input_filepath, delimiter=";")
    
    # Save the DataFrame to a new CSV file using comma as the delimiter
    df.to_csv(output_filepath, index=False)

convert_delimiter("knowledge_base2.csv", "Knowledge_base_comma.csv")
