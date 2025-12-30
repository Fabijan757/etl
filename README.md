Sales Data Analysis – ETL Project (Python + MySQL)

This project demonstrates a complete data workflow, from loading CSV files
to joining data into a single final table in a MySQL database. The goal of
the project is to show how data from multiple sources is processed and
prepared for analysis.

1. Data sources
The project uses three CSV files:

- customers.csv – customer data
- products.csv – product data
- sales.csv – sales data

2. Database and table creation (MySQL)
In MySQL, the following tables are manually created:

- customers
- products
- sales

Each table has predefined columns and data types.

3. Data loading with Python (ETL)
A Python script is used to:

- load data from CSV files
- insert data directly into the MySQL tables (customers, products, sales)

Python is used exclusively for the data ingestion step.

4. Data transformation in MySQL
After all data is loaded:

- SQL JOIN operations are applied
- data from customers, products, and sales tables is combined

A final table called sales_report is created, containing all related data.

5. Result
Data pipeline:
CSV → Python → MySQL tables → SQL JOIN → final sales_report table
