import boto3
s3 = boto3.client('s3')
def lambda_handler(event, context):
    response = s3.list_buckets()
    for bucket in response ['Buckets']:
        name = bucket['Name']
        print(f'Checking bucket:{name}')
        # Fix 1: Block public access if not already blocked
        try:
            bpa = s3.get_public_access_block(Bucket=name)
            config = bpa['PublicAccessBlockConfiguration']
            if not all([
                config['BlockPublicAcls'],
                config['IgnorePublicAcls'],
                config['BlockPublicPolicy'],
                config['RestrictPublicBuckets']
            ]):
                s3.put_public_access_block(
                    Bucket=name,
                    PublicAccessBlockConfiguration={
                        'BlockPublicAcls': True,
                        'IgnorePublicAcls': True,
                        'BlockPublicPolicy': True,
                        'RestrictPublicBuckets': True
                    }
                )
                print(f"  [FIXED] Blocked public access on {name}")
        except Exception:
            s3.put_public_access_block(
                Bucket=name,
                PublicAccessBlockConfiguration={
                    'BlockPublicAcls': True,
                    'IgnorePublicAcls': True,
                    'BlockPublicPolicy': True,
                    'RestrictPublicBuckets': True
                }
            )
            print(f"  [FIXED] Blocked public access on {name}")

        # Fix 2: Enable versioning if not enabled
        versioning = s3.get_bucket_versioning(Bucket=name)
        if versioning.get('Status') != 'Enabled':
            s3.put_bucket_versioning(
                Bucket=name,
                VersioningConfiguration={'Status': 'Enabled'}
            )
            print(f"  [FIXED] Enabled versioning on {name}")

    return {"status": "done"}