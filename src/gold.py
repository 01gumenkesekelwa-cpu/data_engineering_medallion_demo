def aggregate_data(df): 
    """
    Gold Layer: 
    ..............
    This layer prepares business-ready data. 

    Here we:
    - Aggregate sales by product
    - Produce summary matrics

    Gold data is what:
    - Dashboards use 
    - APIs deliver
    - Executives analyse """
    
    summary = (
        df.groupby("product")["total_sales"].sum().reset_index()
    )
    print("Gold Layer Created successfully")
    return summary 