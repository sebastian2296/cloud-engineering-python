import boto3

try:
    from mypy_boto3_s3 import S3Client
except ImportError:
    print("mypy_boto3_s3 is not installed")


def write_s3(bucket_name: str, object_key: str, data: bytes) -> None:
    s3_client: S3Client = boto3.client("s3")
    s3_client.put_object(Bucket=bucket_name, Key=object_key, Body=data)
