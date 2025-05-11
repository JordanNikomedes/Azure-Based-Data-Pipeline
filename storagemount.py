# Databricks notebook source
config = {
    'fs.azure.account.auth.type': 'CustomAccessToken',
    'fs.azure.account.custom.token.provider.class': spark.conf.get('spark.databricks.passthrough.adls.gen2.tokenProviderClassName')
}

dbutils.fs.mount(
    source = 'abfss://bronze@pipelineprodl.dfs.core.windows.net/',
    mount_point = '/mnt/bronze',
    extra_configs = config
)

# COMMAND ----------

dbutils.fs.ls('/mnt/bronze')

# COMMAND ----------

dbutils.fs.mount(
    source = 'abfss://silver@pipelineprodl.dfs.core.windows.net/',
    mount_point = '/mnt/silver',
    extra_configs = config
)

dbutils.fs.mount(
    source = 'abfss://gold@pipelineprodl.dfs.core.windows.net/',
    mount_point = '/mnt/gold',
    extra_configs = config
)