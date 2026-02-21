import pandas as pd 
def load_raw_data(file_path): 
    """
    Bronze Layer: 
    -----------
    This function loads raw data exactly as it is received.
    No cleaning or transformation happens here. 

    In a real workplace, this could come from:
    - An API
    - A database 
    - Cloud storage
    - Streaming service

    The goal of the bronze layer is preservation """

    # Load the raw CSV file 
    df = pd.read_csv(file_path)
    
    print("Bronze Layer Loaded successfully")
    print(f"shape of raw data: {df.shape}")

    return df