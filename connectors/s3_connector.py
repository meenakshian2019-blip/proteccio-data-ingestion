import boto3
import os
from flask import jsonify
from botocore.exceptions import ClientError


def get_s3_client():
    return boto3.client(
        "s3",
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),
        aws_secret_access_key=os.getenv("AWS_SECRET_KEY"),
        region_name=os.getenv("AWS_REGION", "ap-south-1")
    )


def list_buckets():
    """
    List all S3 buckets
    """

    try:
        s3 = get_s3_client()
        response = s3.list_buckets()

        buckets = [bucket["Name"] for bucket in response["Buckets"]]

        return jsonify({
            "buckets": buckets
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


def list_files(bucket_name):
    """
    List files inside bucket
    """

    try:
        s3 = get_s3_client()

        response = s3.list_objects_v2(Bucket=bucket_name)

        files = []

        if "Contents" in response:
            files = [obj["Key"] for obj in response["Contents"]]

        return jsonify({
            "bucket": bucket_name,
            "files": files
        })

    except ClientError as e:
        return jsonify({
            "error": str(e)
        }), 500