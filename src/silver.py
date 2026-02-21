import pandas as pd 
def clean_data(df): 
    """
    Silver Layer: 
    ................
    This layer is responsible for cleaning and standardising data.

    Tasks performed here: 
    - Remove duplicate records 
    - Handle missing values 
    - Create new calculated columns
    - Ensure correct data types 

    The goal is to produce validated, structured data 
    """

    # remove duplicate rows 
    df = df.drop_duplicates()

    #Remove rows where critical fields are missing 
    df = df.dropna(subset= ["quantity","price"])

    #Create a new calculated column
    df["total_sales"]= df["quantity"]* df["price"]

    print("Silver Layer Processed successfully")
    print(f"Shape after cleaning: {df.shape}")

    return df 
