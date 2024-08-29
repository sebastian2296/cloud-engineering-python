import boto3
import pytest
from moto import mock_aws

from tests.consts import TEST_BUCKET_NAME


@pytest.fixture
def mock_fixture():
    with mock_aws():
        s3_client = boto3.client("s3")
        s3_client.create_bucket(Bucket=TEST_BUCKET_NAME)

        yield

        bucket_objs = s3_client.list_objects_v2(Bucket=TEST_BUCKET_NAME)

        for obj in bucket_objs.get("Contents", []):
            s3_client.delete_object(Bucket=TEST_BUCKET_NAME, Key=obj["Key"])

        s3_client.delete_bucket(Bucket=TEST_BUCKET_NAME)
