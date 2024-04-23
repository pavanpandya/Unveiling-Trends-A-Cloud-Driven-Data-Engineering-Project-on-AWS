# Unveiling Trends- Youtube Trends on AWS

## Introduction

YouTube Trends simplifies the way businesses and content creators understand and utilize YouTube. It helps businesses find the best times and places to advertise, while giving content creators insights into what audiences want. Through the project, content creators can easily identify what's trending in their specific region and stay updated on the hottest topics currently circulating on YouTube. With YouTube Insight, users can maximize their online presence by gaining a deeper understanding of their data.

## Dataset

We are using the Kaggle dataset which is given: [Dataset](https://www.kaggle.com/datasets/rsrishav/youtube-trending-video-dataset)

- Each file contains metadata essential for understanding YouTube videos, including details such as the video title, channel title, publication time, tags, views, likes, dislikes, description, comment count, and category ID.
- The dataset is updated daily, ensuring users have access to the latest information and trends on YouTube.
- A category_id field is included in the data, which may vary between different regions.
- To retrieve the categories associated with a specific video, users can refer to the corresponding JSON file provided within the dataset.
- Separate files are available for each region, allowing for region-specific analysis and insights.
- Also we have used the Scraper that scrapes the data at every 7 days of interval and collect the data which will go through our pipeline and can show the visualisation on the Quciksight
- Here is the code for it.
  [Scraper](https://github.com/pavanpandya/Unveiling-Trends-A-Cloud-Driven-Data-Engineering-Project-on-AWS)

## Architecture Overview:

![alt text](Architecture-1.png)

## Technology Stack

- **Amazon S3 (Simple Storage Service)**: Think of it as a secure, massive storage space where your data lives, offering flexibility and reliability. It's like having a super-sized digital warehouse that never runs out of space, with added features like keeping multiple versions of your files and automatically managing old data.
- **AWS IAM (Identity and Access Management)**: Picture it as the guardian of your digital kingdom, ensuring only the right people have access to your resources. It's like having a virtual security team that sets strict rules, allowing only authorized individuals to enter, using fine-tuned permissions and temporary access keys.
- **Amazon QuickSight**: Imagine it as your personal data artist, transforming raw data into stunning visuals and insights. It's like having a magic paintbrush that turns numbers and statistics into interactive graphs and charts, making data exploration a breeze.
- **AWS Glue**: Think of it as your data wizard, automating the tedious tasks of discovering, organizing, and connecting your data. It's like having a diligent assistant that sorts through messy information, cataloging it neatly and preparing it for analysis without you lifting a finger.
- **AWS Lambda**: See it as your on-demand computing powerhouse, ready to spring into action whenever needed. It's like having a fleet of super-fast processors waiting in the wings, triggered by specific events and scaling up or down automatically, so you only pay for what you use.
- **Amazon Athena**: Envision it as your personal data detective, ready to solve any query you throw its way. It's like having a brilliant investigator that can sift through mountains of data stored in Amazon S3, using plain old SQL to uncover valuable insights in seconds.

## Workflow:

1. **AWS IAM User and Role Setup**:

   - Create an IAM user with appropriate permissions and attach a role for accessing AWS services.
   - Configure policies for least privilege access and fine-grained control over resources.

   ![alt text](IAM-1.png)

2. **AWS CLI Setup**:

   - Install and configure the AWS Command Line Interface (CLI) for programmatic access to AWS services.
   - Set default configurations such as AWS region and output format.

   ![alt text](Lambda-1.png)

3. **Data Ingestion**:

   - Use AWS CLI to upload YouTube data files to S3 buckets.
   - Organize data files within S3 buckets based on a specified naming convention.

4. **Data Schema Understanding for both JSON & CSV files**:

   - Configure AWS Glue crawlers to explore raw data stored in S3 buckets and create a database with tables.
   - Run Glue crawlers to discover schema and create tables for JSON and CSV files.

5. **Solving JSON format error using AWS Lambda**:

   - Develop an AWS Lambda function to convert JSON files to Parquet format.
   - Configure Lambda environment variables and AWS SDK layer.
   - Implement data transformations and extract required columns.

6. **Updating the datatype of id in cleansed reference data**:

   - Update the datatype of 'id' to bigint in the Glue catalog table schema.
   - Run the Lambda function again to update the datatype in Parquet files.

7. **Create AWS Glue ETL job for CSV files in raw data**:

   - Develop a Glue ETL job to convert CSV files to Parquet format.
   - Configure data source, transformation, and output settings.
   - Partition the output Parquet files based on regions.

8. **Create AWS Glue crawler for the cleansed parquet files of raw data**:

   - Configure an AWS Glue crawler to explore cleansed Parquet files and create a database with tables.
   - Run the crawler to discover schema and create tables.

9. **Create AWS Glue ETL job for joining cleansed parquet data catalogs**:

   - Develop a Glue ETL job to join data catalogs of cleansed CSV and reference JSON Parquet files.
   - Configure data sources, join conditions, and output settings.
   - Partition the output Parquet files based on regions and category IDs.

10. **Reporting on AWS QuickSight & Querying on AWS Athena**:
    - Utilize AWS Athena to query data stored in the Glue data catalog created for analytics.
    - Create interactive dashboards in AWS QuickSight for visualizing insights and trends in the data.
    - Observe key metrics for running advertisement campaigns on better-performing YouTube videos.
    <!-- <p align="center">
        <img src="docs/athena.png" alt="AWS-athena" width="1050"/>
    </p>

<!-- <p align="center">
    <img src="docs/dashboard-for-youtube.png" alt="dashboard" width="1050"/>
</p>  -->
