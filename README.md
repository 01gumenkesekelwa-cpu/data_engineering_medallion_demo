# 🏗️ Data Engineering Medallion Pipeline (Python)

This project implements a complete **Medallion Architecture (Bronze → Silver → Gold)** data pipeline using modular Python scripts. It demonstrates core data engineering principles including data ingestion, cleaning, transformation, and business-level aggregation.

This repository is designed to showcase **production-minded engineering skills** for early-career data engineering roles.

---

# 📚 Contents

- Overview
- Architecture
- Why This Matters for Data Engineering Roles
- Project Structure
- How to Run
- Technical Walkthrough
- Future Enhancements
- Author

---

# 🔎 Overview

Modern data platforms such as **Databricks**, **Azure Lakehouse**, and **AWS Glue** use a structured approach known as the **Medallion Architecture**:

- **Bronze:** Raw ingestion  
- **Silver:** Cleaning, validation, standardization  
- **Gold:** Business-ready tables  

This project implements a lightweight version of that architecture entirely in Python.

It is intentionally structured like a real-world codebase, using:
- modular script design  
- clear separation of concerns  
- reproducible pipeline orchestration  
- explicit documentation  

---

# 🧱 Architecture

Below is the simplified architecture diagram:

```
                 +----------------------+
                 |    bronze_raw.csv    |
                 | (Raw Input Dataset)  |
                 +----------+-----------+
                            |
                            v
                  [ Bronze Layer ]
                   load_raw_data()
                            |
                            v
                +-----------------------+
                |  silver_cleaned.csv   |
                +-----------------------+
                            |
                            v
                [ Silver Layer ]
                 clean_data()
                            |
                            v
                +-----------------------+
                | gold_aggregated.csv   |
                +-----------------------+
                            |
                            v
                [ Gold Layer ]
                 aggregate_data()
```

---

# ⭐ Why This Matters for Data Engineering Roles

This project demonstrates skills recruiters look for in **real** data engineering candidates:

### ✔ Understanding of modern data architectures  
(especially Databricks-style lakehouse designs)

### ✔ Ability to build modular, scalable data pipelines  
Not just “one big script.”

### ✔ Knowledge of ingestion → cleaning → standardization → aggregation lifecycle  

### ✔ Clean coding and documentation practices  
Exactly what technical leads want to see.

### ✔ Awareness of business-oriented data requirements  
Gold layer != raw data.  
It is **purpose-built data** for downstream consumption.

### ✔ Version-controlled, reproducible project  
Critical for production data engineering.

---

# 📁 Project Structure

```
data-engineering-medallion-demo/
│
├── data/
│   └── bronze_raw.csv
│
├── src/
│   ├── __init__.py
│   ├── bronze.py
│   ├── silver.py
│   └── gold.py
│
├── main.py
└── README.md
```

---

# 🚀 How to Run

### 1️⃣ Create virtual environment

```
python3 -m venv .venv
source .venv/bin/activate
```

### 2️⃣ Install dependencies

```
pip install pandas
```

### 3️⃣ Run the pipeline

```
python main.py
```

Outputs are saved automatically into:

- `data/silver_cleaned.csv`
- `data/gold_aggregated.csv`

---

# 🧪 Technical Walkthrough

### 🥉 Bronze Layer (`bronze.py`)
- Ingests raw CSV  
- Preserves original schema  
- Performs **no transformations**  
- Represents real ingestion from APIs/files/streams  

### 🥈 Silver Layer (`silver.py`)
- Removes duplicates  
- Handles missing values  
- Computes new fields (e.g., `total_sales`)  
- Produces **validated and structured data**

### 🥇 Gold Layer (`gold.py`)
- Aggregates total sales per product  
- Outputs business-ready tables  

### 🎛 Orchestration (`main.py`)
- Calls the entire Bronze → Silver → Gold pipeline  
- Saves outputs  
- Prints status messages  

---

# 🔮 Future Enhancements

- Add PySpark version of pipeline  
- Store Bronze/Silver/Gold data in cloud storage (AWS S3 / Azure Blob)  
- Add logging and exception handling  
- Add unit tests  
- Add CI/CD with GitHub Actions  
- Add SQL-based transformations  
- Add streaming simulation with Kafka  

---

# 👩🏽‍💻 Author  
**Sekelwa Gumenke**  
Early-career Data Engineer | Data Science PGDip (Wits)  
GitHub: https://github.com/01gumenkesekelwa-cpu/SekelwaGumenke-
LinkedIn: https://www.linkedin.com/in/sekelwa-gumenke-323478171
