# 🚖 PySpark Taxi Fare Predictor: Big Data Regression Pipeline

A robust, distributed machine learning pipeline built with **PySpark** to predict taxi fares. This project is specifically architected to perform high-level model comparison and hyperparameter tuning while respecting a **16GB RAM** hardware constraint.

---

## 📖 Project Overview
This repository contains a full end-to-end pipeline—from raw data ingestion and cleaning to model deployment. It solves the regression problem of predicting the `total_amount` of a NYC taxi trip by evaluating the trade-offs between linear models and complex ensemble tree methods.

### Key Features
* **Automated Data Cleaning:** Handles `Null`, `NaN`, and `Infinite` values across distributed partitions.
* **ML Pipeline Architecture:** Encapsulates `VectorAssembler`, `StandardScaler`, and `Regressors` into a single deployable `PipelineModel`.
* **Resource Optimized:** Implements specific Spark configurations (Checkpointing, Bin reduction, Low parallelism) to prevent OOM errors on 16GB RAM.
* **Experimental Benchmarking:** Includes a comparison suite for Linear Regression, Decision Trees, Random Forests, and GBTs.

---

## 📊 The Dataset
This project utilizes the **NYC Yellow Taxi Trip Records**, which provide millions of rows of real-world telemetry data.

### How to Get the Data
1.  **Download:** Visit the [NYC TLC Trip Record Data Website](https://data.cityofnewyork.us/api/views/4b4i-vvec/rows.csv?accessType=DOWNLOAD).
1.   **Aternate** googe-drive [NYC DATA Goolge backup](https://drive.google.com/drive/folders/1i5WQkzUKL47hN4JE5OgiWB3DSp0n2viY?usp=sharing)
2.  **Select:** Download the **Yellow Taxi Trip Records** for any month (e.g., January 2024).
3.  **Format:** The script is optimized for the standard `.parquet` or `.csv` files provided by the city.
4.  **Placement:** Save the file in a folder named `data/raw` in the root directory.

```bash
# Recommended Directory Structure
.
├── data/
│   └── raw/
│       └── yellow_tripdata_2023.parquet
├── models/             # Saved PipelineModels
├── checkpoints/        # GBT Lineage truncation
├── main_pipeline.py    # Main execution script
└── README.md