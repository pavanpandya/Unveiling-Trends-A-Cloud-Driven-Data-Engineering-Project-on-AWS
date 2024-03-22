import os
import urllib.parse
import pandas as pd
import awswrangler as wr

# Retrieve environment variables
S3_CLEANSING_LAYER = os.environ['s3_cleansed_layer']
GLUE_CATALOG_DB_NAME = os.environ['glue_catalog_db_name']
GLUE_CATALOG_TABLE_NAME = os.environ['glue_catalog_table_name']
WRITE_DATA_OPERATION = os.environ['write_data_operation']


def process_json_data(event, context):
    """
    Lambda function designed to process JSON data residing within an S3 bucket, orchestrating the transformation into a Pandas DataFrame. This DataFrame undergoes normalization before being saved as a Parquet file within a distinct S3 bucket. Optionally, the processed data may be cataloged within the AWS Glue service.

    Parameters:
    - event (dict): A dictionary encapsulating details regarding the S3 event that invoked the Lambda function, typically containing metadata about the originating S3 bucket and its objects.
    - context (LambdaContext): An object serving as a runtime provider, furnishing information pertinent to the Lambda function's execution.

    Returns:
    - dict: A dictionary encapsulating the response resulting from the AWS Data Wrangler's write operation.

    Exceptions:
    - Exception: Raised upon encountering errors during the processing of S3 objects or during the writing process to S3. This is intended to prompt AWS Lambda's error handling mechanisms.

    Notable Points:
    - This Lambda function operates on JSON data stored within a specified S3 bucket, converting it into a Pandas DataFrame. Subsequently, relevant columns are extracted and the resultant DataFrame is persisted in Parquet format within another designated S3 bucket.
    - It is imperative to ensure that the requisite environment variables (s3_cleansed_layer, glue_catalog_db_name, glue_catalog_table_name, write_data_operation) are correctly configured prior to invoking this Lambda function.
    """
    try:
        # Get the object from the event
        bucket = event['Records'][0]['s3']['bucket']['name']
        key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')

        # Read JSON data from S3 into a DataFrame
        df_raw = wr.s3.read_json('s3://{}/{}'.format(bucket, key))

        # Normalize DataFrame
        df_normalized = pd.json_normalize(df_raw['items'])

        # Write normalized DataFrame to Parquet file on S3
        wr_response = wr.s3.to_parquet(
            df=df_normalized,
            path=S3_CLEANSING_LAYER,
            dataset=True,
            database=GLUE_CATALOG_DB_NAME,
            table=GLUE_CATALOG_TABLE_NAME,
            mode=WRITE_DATA_OPERATION
        )

        return wr_response

    except Exception as e:
        print(e)
        print(f"Error processing object {key} from bucket {bucket}.")
        raise e
