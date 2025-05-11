# Azure-Based-Data-Pipeline

In this project my aim was to have a greater understanding of building a data pipeline from scratch given some requirements from fake stakeholders to expand my knowledge ready for any real world scenario. Building this pipeline I managed to have a lot more hands on experience with Azure and the intricate details for connecting every service from an on premise server all the way to building dashboards through powerbi. My biggest learning curve was the code put into it, developing the ETL and making sure everything ran smoothly. I think my biggest challenge in this project was using Azure services I had not learnt before, locating what I needed and exploring its full capabilities.

## Table of Contents

- [Business Requirements](#Business-Requirements)
- [Project Overview](#Project-overview)

## Business Requirements

The business has identified a gap in customer demographic, specifically in gender distribution and how it influences product sales. The key requirements include:

1. **Sales by Gender and Product Category**: A dashboard displaying total products sold, total sales revenue and gender split between customers.
2. **Data Filtering**: Ability to filter the data by product category, gender, and date.
3. **User-Friendly Interface**: Stakeholders should have access to an easy-to-use interface for making queries.

## Project Overview

The goal of this project was to extract customer and sales data from an on premise sql server, transform that data within the cloud creating a multi-hop architecture to make sure the data is aggregated and analytic ready. Finally the customer and sales data was then loaded and built into a dashboard to alleviate the current issue. Key vault was used during this project to ensure security and governance.



<p align="center">
  <img src="images/Blank document.jpeg" alt="Diagram" width="750">
</p>

## Technology Used

- **Azure Data Factory**
- **Azure Delta Lake Storage**
- **Azure Databricks**
- **Azure Synapse Analytics**
- **Power Bi**
- **Azure Key Vault**
- **SQL Server(On-Premise)**



## Azure Environment Setup

First within Azure I started by creating a resource group to hold all the resources that I need. I then created the data factory, databricks, synapse, delta lake with bronze, silver and gold folders within the container. Finally I configured the key vault first holding my login for the SQL Server on-premise.

## Data Ingestion

With data ingestion I downloaded both SQL Server and SSMS, then loaded the sample data 'AdventureWorks' onto my machine. I then created a login from SSMS to promote security when linking to the cloud.


<p align="center">
  <img src="images/Screenshot 2025-05-07 125557.png" alt="Login" width="750">
</p>


Finally within Azure Data Factory I created a pipeline to copy the data from the on-premise server to Azure Delta Lake within the bronze folder. The process was to create both a source and a sink within the pipeline to link the service, then iterate through each table using the 'ForEach' activity to make sure I had all the data. The pipeline was then tested and was a success.


<p align="center">
  <img src="images/Screenshot 2025-05-09 123405.png" alt="Linkedservice" width="750">
</p>

<p align="center">
  <img src="images/Screenshot 2025-05-10 102808.png" alt="Pipeline" width="750">
</p>

## Data Transformation

creating a single node cluster and opening a notebook in databricks was the next stage in the process. I first mounted the data so it could be accessed from the Delta Lake Storage, I had mounted all the bronze, silver and gold. 
To clean the format of the customer and sales data, the dates had to be modified so it was in a readable format. Consequently I had made the tables into a dataframe and made sure all tables had a readable timestamp format.


<p align="center">
  <img src="images/Screenshot 2025-05-10 162154.png" alt="transformtables1" width="750">
</p>


<p align="center">
  <img src="images/Screenshot 2025-05-10 162204.png" alt="transformtables2" width="750">
</p>


Once all tables were cleaned and put into the silver folder, I then aggregated the table even more making the column names more readable by applying snake_case to all names. Finally once that was completed, it was then moved into the gold folder within the container.


<p align="center">
  <img src="images/Screenshot 2025-05-11 054929.png" alt="transformtables3" width="750">
</p>


<p align="center">
  <img src="images/Screenshot 2025-05-11 054935.png" alt="transformtables4" width="750">
</p>


<p align="center">
  <img src="images/Screenshot 2025-05-11 055048.png" alt="transformtables5" width="750">
</p>

Moving to Data Factory, an activity was created inside the pipeline for the databricks notebook linking the service.

<p align="center">
  <img src="images/Screenshot 2025-05-11 060418.png" alt="notebook in DF" width="750">
</p>

## Data Loading And Reporting

Azure Synapse was opened and a SQL pool was created to put the tables in the gold folder into views and further analyzed. To quicken the process in this instance I created a pipeline to automatically create views for each table.


<p align="center">
  <img src="images/Screenshot 2025-05-11 063736.png" alt="synapse1" width="750">
</p>


<p align="center">
  <img src="images/Screenshot 2025-05-11 065746.png" alt="synapse2" width="750">
</p>

Finally all tables were uploaded to PowerBi to see a visual representation of the original business requirement.


<p align="center">
  <img src="images/dashboard.pdf" alt="dashboard" width="750">
</p>


## Security and Governance

Throughout the project I had been using key vault to hold any sensitive information including tokens that were generated through databricks. Key vault was applied throughout the pipeline in Data Factory when linking services to ensure all data was secure. I also used role-based access control (RBAC) using Azure Entra ID the emulate a life based scenario.
