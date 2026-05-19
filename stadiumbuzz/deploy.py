import boto3
import time
import os
import mimetypes

BUCKET_NAME = 'stadiumbuzz-s3-website-bucket'
DISTRIBUTION_ID = 'E12D0IP4OCGZBJ'
PROFILE = 'limonlab'
REGION = 'eu-north-1'
WEBSITE_FOLDER = 'website'

session = boto3.Session(profile_name=PROFILE, region_name=REGION)
s3 = session.client("s3")

upload_success = False

try:
    for filename in os.listdir(WEBSITE_FOLDER):
        local_path = os.path.join(WEBSITE_FOLDER, filename)
        content_type, _ = mimetypes.guess_type(filename)
        if content_type is None:
            content_type = 'application/octet-stream'
        s3.upload_file(
            local_path,
            BUCKET_NAME,
            filename,
            ExtraArgs={'ContentType': content_type}
        )
        print(f"Uploaded {filename} ({content_type}) to {BUCKET_NAME}")
    upload_success = True
except Exception as e:
    print(f"Upload failed: {e}")

try:
    if upload_success:
        cloudfront = session.client("cloudfront")
        response = cloudfront.create_invalidation(
            DistributionId=DISTRIBUTION_ID,
            InvalidationBatch={
                'Paths': {
                    'Quantity': 1,
                    'Items': ['/*']
                },
                'CallerReference': str(time.time())
            }
        )
        print("Cache invalidation created:", response['Invalidation']['Id'])
except Exception as e:
    print(f"Invalidation failed: {e}")