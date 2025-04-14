import boto3
import requests
import logging
import sys
from botocore.exceptions import ClientError

def create_presigned_url(bucket_name, object_name, expiration=3600):
    s3_client = boto3.client('s3', region_name='us-east-1')
    try:
        response = s3_client.generate_presigned_url(
            'get_object',
            Params={'Bucket': bucket_name, 'Key': object_name},
            ExpiresIn=expiration,
        )
    except ClientError as e:
        logging.error(e)
        return None
    return response

def main():
    if len(sys.argv) < 4:
        print("Usage: python3 upload_and_presign.py <image_url> <bucket_name> <object_name> [expiration_seconds]")
        sys.exit(1)

    image_url = sys.argv[1]
    bucket = sys.argv[2]
    object_name = sys.argv[3]
    expiration = int(sys.argv[4]) if len(sys.argv) > 4 else 604800

    print(f"Downloading image from: {image_url}")
    response = requests.get(image_url)
    if response.status_code != 200:
        print("Failed to download the image.")
        sys.exit(1)

    with open(object_name, 'wb') as f:
        f.write(response.content)
    print("Image downloaded successfully.")

    print(f"Uploading {object_name} to bucket {bucket}...")
    s3_client = boto3.client('s3', region_name='us-east-1')
    try:
        with open(object_name, 'rb') as f:
            s3_client.put_object(
                Bucket=bucket,
                Key=object_name,
                Body=f,
                ContentType='image/jpeg'
            )
    except ClientError as e:
        logging.error(e)
        print("Upload failed.")
        sys.exit(1)

    print("Upload successful.")
    url = create_presigned_url(bucket, object_name, expiration)
    if url:
        print(f"Presigned URL (expires in {expiration} seconds):\n{url}")
    else:
        print("Failed to generate presigned URL.")

if __name__ == "__main__":
    main()
