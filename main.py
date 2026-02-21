from src.bronze import load_raw_data
from src.silver import clean_data
from src.gold import aggregate_data
def run_pipeline():
    """
    Orchestates the entire medallion pipeline.
    This function connects all layers together."""
    #Step 1: Load raw data 
    raw_data = load_raw_data("data/bronze_raw.csv")

    #Step 2: Clean and transform 
    cleaned_data = clean_data(raw_data)

    #Step 3: Create business-level summary 
    final_data= aggregate_data(cleaned_data)

    #save outputs 
    cleaned_data.to_csv("data/silver_cleaned.csv", index = False)
    final_data.to_csv("data/gold_aggregated.csv", index= False)

    print("Pipeline executed successfully.")

if __name__ =="__main__":
    run_pipeline()
