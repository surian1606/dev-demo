import os
import boto3
from botocore.exceptions import ClientError
import datetime
import time

def upload_files_to_s3(local_directory, bucket_name, s3_prefix=''):
    """
    Upload files from a local directory to an S3 bucket while preserving original file creation times.
    
    :param local_directory: Path to the local directory containing files to upload
    :param bucket_name: Name of the S3 bucket
    :param s3_prefix: Optional prefix/folder path in the S3 bucket
    """
    # Create S3 client
    s3_client = boto3.client('s3')
    
    # Walk through the directory
    for root, dirs, files in os.walk(local_directory):
        for file in files:
            # Full local file path
            local_path = os.path.join(root, file)
            
            # Relative path for S3 key (preserving directory structure)
            relative_path = os.path.relpath(local_path, local_directory)
            s3_key = os.path.join(s3_prefix, relative_path).replace('\\', '/')
            
            try:
                # Get file creation time
                file_stats = os.stat(local_path)
                creation_time = datetime.datetime.fromtimestamp(file_stats.st_ctime)
                
                # Upload file to S3
                s3_client.upload_file(local_path, bucket_name, s3_key)
                
                # Set custom metadata for original creation time
                s3_client.copy_object(
                    Bucket=bucket_name,
                    CopySource={'Bucket': bucket_name, 'Key': s3_key},
                    Key=s3_key,
                    Metadata={
                        'original-creation-time': creation_time.isoformat(),
                        'original-creation-timestamp': str(file_stats.st_ctime)
                    },
                    MetadataDirective='REPLACE'
                )
                
                print(f"Successfully uploaded {local_path} to s3://{bucket_name}/{s3_key}")
                print(f"Original creation time: {creation_time}")
            
            except ClientError as e:
                print(f"Error uploading {local_path}: {e}")
            except Exception as e:
                print(f"Unexpected error with {local_path}: {e}")

def main():
    # Configuration - replace these with your actual values
    LOCAL_DIRECTORY = 'C:/Users/suriasya/Pictures'
    BUCKET_NAME = 'surian-dev-demo-bucket'
    S3_PREFIX = ''  # Optional: upload to a specific folder in S3
    
    # Ensure AWS credentials are configured (via AWS CLI, environment variables, or credentials file)
    upload_files_to_s3(LOCAL_DIRECTORY, BUCKET_NAME, S3_PREFIX)

if __name__ == '__main__':
    main()
