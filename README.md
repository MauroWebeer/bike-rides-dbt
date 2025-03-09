# 🚴‍♂️ Bike Rides DBT Project

A data pipeline project using **PostgreSQL** and **DBT** to analyze bike ride data. This project demonstrates how to create a **data warehouse** with fact and dimension tables, and how to perform analytics such as **average revenue by day**.

---

## 🛠️ Prerequisites

Before running this project, ensure you have the following installed:

- **PostgreSQL**: A relational database to store and query your data.
- **DBT (Data Build Tool)**: A tool for transforming data in your warehouse.
- **Python**: For running scripts to populate the database.
- **Python Dependencies**:
    - psycopg2 (PostgreSQL connector)

---

## 🔢 Database Setup

### 1. SQL Script to Create PostgreSQL Tables

The database consists of four main tables:

- **rides**: Stores information about each bike ride.
- **users**: Contains details of users who rented bikes.
- **bikes**: Information about available bikes.
- **payments**: Records transactions for each ride.

To create these tables, run the provided SQL script:

```bash
psql -U your_username -d your_database -f scripts/create_tables.sql
```

### 2. Python Script to Populate Tables

A Python script (`insert_data.py`) is provided to insert sample data into the tables.
Run it using:

```bash
python3 scripts/insert_data.py
```

This script will:
- Connect to your PostgreSQL database.
- Generate and insert mock data for users, bikes, rides, and payments.

---

## 📚 DBT Models

The DBT project is structured as follows:

### 1. **Dimension Tables (Views)**

These are created as **views** to store descriptive details:
- `dim_users`: Contains user-related details.
- `dim_bikes`: Provides information about bikes.
- `dim_payments`: Provides information about payments. 

### 2. **Fact Table (Table)**

A **fact table** aggregates ride and payment information:
- `fact_rides`: Combines ride details, user info, bike data, and payment amounts.

### 3. **Analyses (Tables)**

DBT also runs predefined analyses, such as:
- `avg_ride_duration_per_user`: Calculates the average ride duration per user.
- `revenue_by_day`: Computes total revenue grouped by day.
- `ride_count_by_bike`: Counts the number of rides per bike.
- `total_revenue_by_user`: Computes total revenue per user.

---

## 🚀 Running DBT

### 1. Install DBT

If you haven't installed DBT yet, run:

```bash
pip install dbt-postgres
```

### 2. Run DBT Models

Execute the DBT models to create dimensions, facts, and analyses:

```bash
dbt run
```

### 3. Run DBT Tests

Ensure the models are working correctly:

```bash
dbt test
```

### 4. View Results

Once the transformations are complete, you will be able to see the fact and dimension tables in PostgreSQL.

---

This project demonstrates a structured approach to **data modeling** using DBT and PostgreSQL. Enjoy exploring the data! 🚀




