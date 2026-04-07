import boto3
s3 = boto3.client('s3')
response = s3.list_buckets()
total = 0
risks = 0
for bucket in response['Buckets']:
    name = bucket['Name']
    total += 1
    print(f"\nBucket: {name}")
    # Check 1: Public access block
    try:
        bpa = s3.get_public_access_block(Bucket=name)
        config = bpa['PublicAccessBlockConfiguration']
        all_blocked = all([
            config['BlockPublicAcls'],
            config['IgnorePublicAcls'],
            config['BlockPublicPolicy'],
            config['RestrictPublicBuckets']
        ])
        if all_blocked:
            print("  [OK] Public access is blocked")
        else:
            print("  [RISK] Public access is NOT fully blocked")
            risks += 1
    except Exception:
        print("  [RISK] No public access block configured")
        risks += 1
    # Check 2: Versioning
    versioning = s3.get_bucket_versioning(Bucket=name)
    status = versioning.get('Status', 'Disabled')
    if status == 'Enabled':
        print("  [OK] Versioning is enabled")
    else:
        print("  [RISK] Versioning is not enabled")
        risks += 1
    # Check 3: Encryption
    try:
        s3.get_bucket_encryption(Bucket=name)
        print("  [OK] Encryption is enabled")
    except Exception:
        print("  [RISK] Encryption is not enabled")
        risks += 1

    # Check 4: Access logging
    logging_status = s3.get_bucket_logging(Bucket=name)
    if 'LoggingEnabled' in logging_status:
        print("  [OK] Access logging is enabled")
    else:
        print("  [RISK] Access logging is not enabled")
        risks += 1
print(f"\n--- Scan Complete ---")
print(f"Buckets scanned: {total}")
print(f"Risks found: {risks}")

