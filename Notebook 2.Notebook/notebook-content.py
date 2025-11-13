# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "68fcb25d-6c67-475f-a14d-080cfb7528a4",
# META       "default_lakehouse_name": "",
# META       "default_lakehouse_workspace_id": "",
# META       "known_lakehouses": [
# META         {
# META           "id": "68fcb25d-6c67-475f-a14d-080cfb7528a4"
# META         },
# META         {
# META           "id": "4ebb9d96-8195-4e99-a218-9373bb4e7b80"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!
data = [(101,'chakri'),(102,'kp'),(103,'dky'),(104,'vk')]
columns = ["Name", "Age"]
# spark.createDataFrame(data, columns)
df = spark.createDataFrame(data,columns)
# df.show()
# df.display()
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!
data = [(101,'chakri'),(102,'kp'),(103,'dky'),(104,'vk')]
columns = ["Name", "Age"]
# spark.createDataFrame(data, columns)
df1 = spark.createDataFrame(data,columns)
# df.show()
# df.display()
display(df1)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!
data = [(101,'chakri'),(102,'kp'),(103,'dky'),(104,'vk')]
columns = ["Name", "Age"]
# spark.createDataFrame(data, columns)
df = spark.createDataFrame(data,columns)
# df.show()
# df.display()
# display(df)
# df.printSchema
# df.select('Name','Age').show()
# df.show(1)
# df.filter()
df.filter(df.Name > 25).show()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df_csv = spark.read.option("header", True).option("inferSchema", True).csv("abfss://container@lakehouse_account.dfs.fabric.microsoft.com/path/to/DWSSISLoad.csv")



# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
