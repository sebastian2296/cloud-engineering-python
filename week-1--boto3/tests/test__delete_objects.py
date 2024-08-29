"""Test cases for `s3.delete_objects`."""

from files_api.s3.delete_objects import delete_s3_object
from files_api.s3.read_objects import object_exists_in_s3
from files_api.s3.write_s3 import write_s3
from tests.consts import TEST_BUCKET_NAME


def test_delete_existing_s3_object(mock_fixture: None):
    write_s3(TEST_BUCKET_NAME, "sample.txt", b"bla")
    assert object_exists_in_s3(TEST_BUCKET_NAME, "sample.txt")
    delete_s3_object(TEST_BUCKET_NAME, "sample.txt")
    assert not object_exists_in_s3(TEST_BUCKET_NAME, "sample.txt")


def test_delete_nonexistent_s3_object(mock_fixture: None):
    assert not object_exists_in_s3(TEST_BUCKET_NAME, "sample.txt")
    delete_s3_object(TEST_BUCKET_NAME, "sample.txt")
    assert not object_exists_in_s3(TEST_BUCKET_NAME, "sample.txt")
