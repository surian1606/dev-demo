import os
import boto3
from botocore.exceptions import ClientError
import datetime
import time
import argparse

def upload_files_to_s3(local_directory, bucket_name, s3_prefix=''):
    """
    Upload files from a local directory to an S3 bucket while preserving original file creation times.
    
    :param local_directory: Path to the local directory containing files to upload
    :param bucket_name: Name of the S3 bucket
    :param s3_prefix: Optional prefix/folder path in the S3 bucket
    """
    s3_client = boto3.client('s3')
    
    for root, dirs, files in os.walk(local_directory):
        for file in files:
            local_path = os.path.join(root, file)
            relative_path = os.path.relpath(local_path, local_directory)
            s3_key = os.path.join(s3_prefix, relative_path).replace('\\', '/')
            
            try:
                file_stats = os.stat(local_path)
                creation_time = datetime.datetime.fromtimestamp(file_stats.st_ctime)
                
                s3_client.upload_file(local_path, bucket_name, s3_key)
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
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Upload files to S3 bucket with metadata')
    
    # Add arguments
    parser.add_argument('--directory', '-d',
                        required=True,
                        help='Local directory path containing files to upload')
    
    parser.add_argument('--bucket', '-b',
                        required=True,
                        help='Name of the S3 bucket')
    
    parser.add_argument('--prefix', '-p',
                        default='',
                        help='Optional S3 prefix (folder path)')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Validate directory exists
    if not os.path.isdir(args.directory):
        print(f"Error: Directory '{args.directory}' does not exist")
        return
    
    # Execute upload
    upload_files_to_s3(args.directory, args.bucket, args.prefix)

if __name__ == '__main__':
    main()
