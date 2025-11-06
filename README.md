# 🛍️ Retail Order Data Analysis Project

A Python + SQL project to analyze retail order data, derive business insights, and optimize sales strategies.

## 📊 Overview

This project demonstrates an end-to-end data pipeline:  
- **Data Cleaning & Transformation** using Python (`pandas`)
- **Data Loading** into SQL Server via `SQLAlchemy`
- **Business Insights** extraction using complex SQL queries

## 🧰 Technologies Used

- **Python 3**
  - pandas
  - sqlalchemy
- **SQL Server**
- **Tools**: Jupyter Notebook / VS Code

## 📁 Data Source

- Public dataset from [Kaggle](https://www.kaggle.com/datasets/ankitbansal06/retail-orders) (Retail Orders)
- Format: CSV

### Columns Included:
- `Order Id`  
- `Order Date`  
- `Ship Mode`  
- `Segment`  
- `Country`  
- `City`  
- `State`  
- `Postal Code`  
- `Region`  
- `Category`  
- `Sub Category`  
- `Product Id`  
- `Cost Price`  
- `List Price`  
- `Quantity`  
- `Discount Percent`

## 📌 Key Insights Derived

- 🔝 Top 10 revenue-generating products  
- 🌍 Region-wise top 5 selling products  
- 📈 Monthly sales growth comparison (2022 vs 2023)  
- 🗓️ Best-selling month per category  
- 💸 Highest profit growth sub-category in 2023  

## ▶️ Running the Project

Follow these steps to set up and run the project locally:

1. **Install Required Python Packages**  
   Make sure you have Python 3 installed. Then, install the dependencies:
   ```bash
   pip install pandas 
   pip install sqlalchemy pyodbc
   ```
   
2. Prepare the database
- Download the dataset from Kaggle (Retail Order Dataset)
- Save the CSV file into the data/ folder of the project (create the folder if needed)

3. Configure Database Connection
- Ensure SQL Server is running on your local machine or a remote server
- In the Python script (data_processing_and_load.py), update the DATABASE_URL variable with your database connection string in the following format:

 **mssql+pyodbc://username:password@server_name/database_name?driver=ODBC+Driver+17+for+SQL+Server**

- Make sure the correct ODBC driver is installed on your machine.

4. Run the Python Script
- This will clean the data and load it into your SQL Server database:
   ```bash
	python order_data_analysis.py
   ```
5. Run SQL analysis queries
- Open order_details_analysis.sql in SQL Server Management Studio (SSMS)
- Execute the queries to extract key insights from the loaded data

