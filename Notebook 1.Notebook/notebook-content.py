# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "4ebb9d96-8195-4e99-a218-9373bb4e7b80",
# META       "default_lakehouse_name": "Trail_lkh",
# META       "default_lakehouse_workspace_id": "d2a7c555-1ac1-423f-995d-ae6ff8e4fb51",
# META       "known_lakehouses": [
# META         {
# META           "id": "4ebb9d96-8195-4e99-a218-9373bb4e7b80"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

df = spark.read.format("com.crealytics.spark.excel") \
    .option("dataAddress", "'Sheet1 (2)'!A1") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load("Files/Audit_Stage_Excel_filters.xlsx")  # Adjust the path to your Fabric Lakehouse or OneLake file


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from pyspark.sql.functions import col,dense_rank
from pyspark.sql.window import Window

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

import pandas as pd

# Step 1: Read Excel file with all columns as strings
pdf = pd.read_excel(
    "abfss://chakri_ws@onelake.dfs.fabric.microsoft.com/Trail_lkh.Lakehouse/Files/Audit_Stage_Excel_filters.xlsx",
    sheet_name="Sheet1 (2)",
    dtype=str
)

# Step 2: Convert to Spark DataFrame
df = spark.createDataFrame(pdf)

window_spec = Window.partitionBy("CLIENT", "COMMUNITY")
df1 = df.withColumn("row_num", dense_rank().over(window_spec)).filter(col("count") == 2)

# Step 4: Display the grouped result
display(df1)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from pyspark.sql import Window
from pyspark.sql.functions import col, count, dense_rank

# Window spec partitioned by CLIENT and COMMUNITY
window_spec = Window.partitionBy("CLIENT", "COMMUNITY")
# Step 1: Read Excel file with all columns as strings
pdf = pd.read_excel(
    "abfss://chakri_ws@onelake.dfs.fabric.microsoft.com/Trail_lkh.Lakehouse/Files/Audit_Stage_Excel_filters.xlsx",
    sheet_name="Sheet1 (2)",
    dtype=str
)

# Step 2: Convert to Spark DataFrame
df = spark.createDataFrame(pdf)
# Add a count column that counts rows per group
df_with_count = df.withColumn("group_count", count("*").over(window_spec))

# Filter where count = 2
df_filtered = df_with_count.filter(col("group_count") == 2)

display(df_filtered)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

xls = pd.ExcelFile("/lakehouse/default/Files/Audit_Stage_Excel_filters.xlsx")
print(xls.sheet_names)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
