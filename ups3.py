from pprint import pprint
import boto3
import pathlib
import os

# Upload to S3
def uploadtoS3(object_name):
    s3 = boto3.client("s3")
    bucket_name = "rep-scan-results"
    file_name = os.path.join(pathlib.Path(__file__).parent.resolve(), object_name)

    response = s3.upload_file(file_name, bucket_name, object_name)
    pprint(response)

uploadtoS3("resultVT.json")
uploadtoS3("resultUS.json")

print("Both files were sucessfully uploaded to S3 bucked named rep-scan-results")