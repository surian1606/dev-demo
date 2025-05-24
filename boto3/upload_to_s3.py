import boto3
import os
import sys

def upload_file_to_s3(file_path, bucket_name, object_name=None):
    """
    Upload a file to an S3 bucket
    
    :param file_path: File to upload
    :param bucket_name: Bucket to upload to
    :param object_name: S3 object name. If not specified, file_name is used
    :return: True if file was uploaded, else False
    """
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_path)
    
    # Upload the file
    s3_client = boto3.client('s3')
    try:
        s3_client.upload_file(file_path, bucket_name, object_name)
        print(f"Successfully uploaded {file_path} to {bucket_name}/{object_name}")
        return True
    except Exception as e:
        print(f"Error uploading file: {e}")
        return False

def main():
    # Define bucket name
    bucket_name = "demo-21052025"
    
    # Check if file path is provided as command line argument
    if len(sys.argv) < 2:
        print("Usage: python upload_to_s3.py <file_path> [object_name]")
        return
    
    file_path = sys.argv[1]
    
    # Check if object name is provided
    object_name = None
    if len(sys.argv) >= 3:
        object_name = sys.argv[2]
    
    # Upload file
    upload_file_to_s3(file_path, bucket_name, object_name)

if __name__ == "__main__":
    main()