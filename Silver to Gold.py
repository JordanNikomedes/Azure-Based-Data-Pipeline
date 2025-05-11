# Databricks notebook source
# MAGIC %md
# MAGIC # Single Column Transformation

# COMMAND ----------

df = spark.read.format('delta').load('/mnt/silver/SalesLT/Address/')

# COMMAND ----------

from pyspark.sql.functions import col

def rename_columns_to_snake_case(df):

    column_names = df.columns

    rename_map = {}

    for old_col_name in column_names:
        new_col_name = ''.join([
            '_' + char.lower() if (
                char.isupper()
                and idx > 0
                and not old_col_name[idx - 1].isupper()
            ) else char.lower()
            for idx, char in enumerate(old_col_name)
        ]).lstrip('_')

        if new_col_name in rename_map.values():
            raise ValueError(f'Duplicate column name found while renaming: {new_col_name}')

        rename_map[old_col_name] = new_col_name


    for old_col_name, new_col_name in rename_map.items():
        df = df.withColumnRenamed(old_col_name, new_col_name)

    return df

# COMMAND ----------

df = rename_columns_to_snake_case(df)

# COMMAND ----------

display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC # Transformation On All Tables

# COMMAND ----------

table_name = []

for i in dbutils.fs.ls('/mnt/silver/SalesLT'):
    table_name.append(i.name.split('.')[0])

table_name

# COMMAND ----------

for name in table_name:
    path = '/mnt/silver/SalesLT/' + name
    print(path)
    df = spark.read.format('delta').load(path)

    df = rename_columns_to_snake_case(df)

    output_path = '/mnt/gold/SalesLT/' + name + '/'

    df.write.mode('overwrite').format('delta').save(output_path)

# COMMAND ----------

display(df)

# COMMAND ----------

