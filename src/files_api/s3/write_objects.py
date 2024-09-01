from typing import Optional

import boto3

try:
    from mypy_boto3_s3 import S3Client
except ImportError:
    print("mypy_boto3_s3 is not installed")


def upload_s3_object(
    bucket_name: str,
    object_key: str,
    data: bytes,
    content_type: Optional[str] = None,
) -> None:
    content_type = content_type if content_type is not None else "application/octet-stream"
    s3_client: S3Client = boto3.client("s3")
    s3_client.put_object(
        Bucket=bucket_name,
        Key=object_key,
        Body=data,
        ContentType=content_type,
    )
