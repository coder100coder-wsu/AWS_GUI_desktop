import logging
import boto3
from botocore.exceptions import ClientError
import os
####################################
import pprint
pp = pprint.PrettyPrinter(indent=4)
####################################


def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: 0 if file was uploaded, else -1
    """
    # Get s3 client
    s3_client = boto3.client('s3')

    # buckets_listing = s3_client.list_buckets()
    # pp.pprint(buckets_listing)

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    try:
        response_upload_file = s3_client.upload_file(file_name, bucket, object_name)
        if response_upload_file is None:
            print("func_response below >>>>> ")
            print("success, uploaded file")
    except ClientError as e:
        logging.error(e)
        print("error= ", e)
        return -1
    return 0

# # local func call
# file_path = "D:\\2_general_repo\\aws_s3_boto3\\requirements.txt"
# # print("file_path = ", file_path)
# file_name = os.path.basename(file_path)
#
# response_upload_file = upload_file(file_name= file_name,
#                         bucket= 'boto3-bucket-1',
#                         object_name=file_name)

# print("func_response below >>>>> ")
# if response_upload_file is None:
#     print("success, uploaded file")





