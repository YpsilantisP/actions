import os
import time

import boto3
import pytest
from botocore.exceptions import ClientError

DYNAMODB_ENDPOINT = os.environ.get("DYNAMODB_ENDPOINT", "http://localhost:8000")

@pytest.fixture(scope="module")
def dynamodb_client():
    """Return a low-level DynamoDB client configured for the local endpoint."""
    return boto3.client(
        "dynamodb",
        region_name="us-west-2",
        aws_access_key_id="fakeAccessKey",
        aws_secret_access_key="fakeSecretKey",
        endpoint_url=DYNAMODB_ENDPOINT
    )


@pytest.fixture(scope="module")
def test_connection(dynamodb_client):
    assert dynamodb_client is not None


# @pytest.fixture(scope="module")
# def test_table(dynamodb_client):
#     """Create and yield a DynamoDB table for testing, then clean up."""
#     table_name = "MyTestTable"
#     # Create the table
#     try:
#         dynamodb_client.create_table(
#             TableName=table_name,
#             AttributeDefinitions=[
#                 {"AttributeName": "PK", "AttributeType": "S"}
#             ],
#             KeySchema=[
#                 {"AttributeName": "PK", "KeyType": "HASH"}
#             ],
#             ProvisionedThroughput={
#                 "ReadCapacityUnits": 5,
#                 "WriteCapacityUnits": 5
#             },
#         )
#         # Wait a bit for the table to become active
#         waiter = dynamodb_client.get_waiter("table_exists")
#         waiter.wait(TableName=table_name)
#     except ClientError as e:
#         raise RuntimeError(f"Failed to create table: {e}")
#
#     yield table_name
#
#     # Clean up
#     dynamodb_client.delete_table(TableName=table_name)
#     waiter = dynamodb_client.get_waiter("table_not_exists")
#     waiter.wait(TableName=table_name)


# def test_put_and_get_item(dynamodb_client, test_table):
#     """Simple test: write an item and read it back."""
#     table_name = test_table
#
#     # Put an item
#     dynamodb_client.put_item(
#         TableName=table_name,
#         Item={
#             "PK": {"S": "test-pk"},
#             "Data": {"S": "Hello, DynamoDB Local!"},
#         }
#     )
#
#     # Retrieve it
#     response = dynamodb_client.get_item(
#         TableName=table_name,
#         Key={"PK": {"S": "test-pk"}}
#     )
#     item = response.get("Item")
#     assert item is not None
#     assert item["Data"]["S"] == "Hello, DynamoDB Local!"
