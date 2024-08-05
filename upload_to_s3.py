import os
import json
import boto3
from datetime import datetime

# Get invocation_id from manifest.json
current_dir = os.path.dirname(os.path.abspath(__file__))
MANIFEST_PATH = 'target/manifest.json'
fill_path = os.path.join(current_dir, MANIFEST_PATH)
with open(fill_path, 'r') as file:
    data = json.load(file)
    invocation_id = data.get('metadata', {}).get('invocation_id', None)

# Upload to S3
BUCKET_NAME = os.environ['S3_BUCKET_NAME']
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
current_date_str = datetime.now().strftime('%Y-%m-%d')
object_path = f'manifest/{current_date_str}/{invocation_id}'

print(f'Uploading to {object_path}')
s3 = boto3.client('s3',
                aws_access_key_id=AWS_ACCESS_KEY_ID,
                aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
s3.upload_file(fill_path, BUCKET_NAME, object_path)
print('Success!')