"""Test cases for `s3.read_objects`."""

import boto3

from files_api.s3.read_objects import (
    fetch_s3_objects_metadata,
    fetch_s3_objects_using_page_token,
    object_exists_in_s3,
)
from tests.consts import TEST_BUCKET_NAME


def test_object_exists_in_s3(mock_fixture: None):
    s3_client = boto3.client("s3")
    s3_client.put_object(Bucket=TEST_BUCKET_NAME, Key="test_key.txt", Body="test_body")
    assert object_exists_in_s3(bucket_name=TEST_BUCKET_NAME, object_key="test_key.txt") is True
    assert object_exists_in_s3(bucket_name=TEST_BUCKET_NAME, object_key="test_key_non_existent.txt") is False


def test_pagination(mock_fixture: None):
    s3_client = boto3.client("s3")
    for i in range(1, 6):
        s3_client.put_object(
            Bucket=TEST_BUCKET_NAME,
            Key=f"test_file_{i}.txt",
            Body=f"test_body_{i}",
        )

    result, continuation_token = fetch_s3_objects_metadata(
        bucket_name=TEST_BUCKET_NAME,
        max_keys=2,
    )

    assert len(result) == 2
    assert result[0]["Key"] == "test_file_1.txt"
    assert result[1]["Key"] == "test_file_2.txt"

    result, continuation_token = fetch_s3_objects_using_page_token(
        bucket_name=TEST_BUCKET_NAME,
        continuation_token=continuation_token,
        max_keys=2,
    )

    assert len(result) == 2
    assert result[0]["Key"] == "test_file_3.txt"
    assert result[1]["Key"] == "test_file_4.txt"

    result, continuation_token = fetch_s3_objects_using_page_token(
        bucket_name=TEST_BUCKET_NAME,
        continuation_token=continuation_token,
        max_keys=2,
    )

    assert len(result) == 1
    assert continuation_token is None


def test_mixed_page_sizes(mocked_aws: None): ...


def test_directory_queries(mocked_aws: None): ...
