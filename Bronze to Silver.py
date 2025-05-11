# Databricks notebook source
dbutils.fs.ls('/mnt/bronze/SalesLT')

# COMMAND ----------

df = spark.read.format('parquet').load('/mnt/bronze/SalesLT/Address/Address.parquet')

# COMMAND ----------

display(df)

# COMMAND ----------

from pyspark.sql.functions import from_utc_timestamp, date_format
from pyspark.sql.types import TimestampType

df = df.withColumn('ModifiedDate', date_format(from_utc_timestamp(df['ModifiedDate'].cast(TimestampType()), 'UTC'), 'yyyy-mm-dd'))

# COMMAND ----------

display(df)

# COMMAND ----------

dbutils.fs.ls('/mnt/silver/SalesLT')

# COMMAND ----------

# MAGIC %md
# MAGIC # Date Transformation For All Tables

# COMMAND ----------

table_name = []

for i in dbutils.fs.ls('/mnt/bronze/SalesLT/'):
    table_name.append(i.name.split('/')[0])

table_name

# COMMAND ----------

from pyspark.sql.functions import from_utc_timestamp, date_format
from pyspark.sql.types import TimestampType

for i in table_name:
    path = '/mnt/bronze/SalesLT/' + i + '/' + i +'.parquet'
    df = spark.read.format('parquet').load(path)
    column = df.columns

    for col in column:
        if "Date" in col or "date" in col:
            df = df.withColumn(col, date_format(from_utc_timestamp(df[col].cast(TimestampType()), "UTC"), "yyyy-MM-dd"))
    
    output_path = '/mnt/silver/SalesLT/' + i + '/'
    df.write.format('delta').mode('overwrite').save(output_path)


# COMMAND ----------

display(df)

# COMMAND ----------

