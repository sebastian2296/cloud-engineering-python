import boto3

from files_api.s3.write_objects import write_s3
from tests.consts import TEST_BUCKET_NAME

try:
    from mypy_boto3_s3 import S3Client
except ImportError:
    ...


def test_write_s3(mock_fixture: None) -> None:
    object_key = "test_key"
    test_data = b"test_data"
    write_s3(bucket_name=TEST_BUCKET_NAME, object_key=object_key, data=test_data)

    client: S3Client = boto3.client("s3")
    response = client.get_object(Bucket=TEST_BUCKET_NAME, Key=object_key)
    assert response["Body"].read() == test_data
    assert response["ContentType"] == "binary/octet-stream"
