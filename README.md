# python-aws-automation

Python scripts for automating AWS infrastructure tasks using boto3.

---

## Scripts

### ec2_report.py
Fetches all EC2 instances and saves a detailed report to `ec2_report.json`.

**Collects per instance:**
- Instance ID
- Name (from tags, defaults to "No Name" if missing)
- State (running/stopped)
- Instance type
- Launch time
- Region (auto-detected from AWS config)

**Features:**
- Error handling per instance
- Prints report to terminal
- Saves report to ec2_report.json

---

### s3_report.py
Lists all S3 buckets and their objects with sizes and last modified dates.

---

## stadiumbuzz/ — Deployment automation for aws-production-static-site

Scripts that automate the deployment workflow for the [aws-production-static-site](https://github.com/billal4232/aws-production-static-site) project.

### stadiumbuzz/deploy.py
Uploads all website files from the `website/` folder to S3 and invalidates the CloudFront cache automatically.

**What it does:**
- Loops through all files in `website/` folder
- Detects correct content-type per file (html, css, js, etc.)
- Uploads each file to S3 private bucket
- Creates CloudFront cache invalidation after successful upload
- Skips invalidation if upload fails

**Features:**
- Auto content-type detection using `mimetypes`
- Error handling for both upload and invalidation
- Upload flag prevents invalidation on failed deployments

**Deployment flow:**
```
website/ folder
    ↓
Upload all files to S3 (with correct content-type)
    ↓
Invalidate CloudFront cache
    ↓
Updated site live globally
```

---

## Requirements
- Python 3
- boto3
- AWS CLI configured with named profile

## Setup
```bash
pip install boto3 --break-system-packages
```

## How to Run
```bash
# EC2 report
python3 ec2_report.py

# S3 report
python3 s3_report.py

# Deploy stadiumbuzz website
cd stadiumbuzz
python3 deploy.py
```

## IAM Permissions Required
- `ec2:DescribeInstances`
- `s3:ListBuckets`
- `s3:PutObject`
- `cloudfront:CreateInvalidation`

## What I Learned
- AWS response structure — nested Reservations and Instances
- Extracting name from Tags list using loop and condition
- Dynamic region detection from AWS config
- Separating concerns using functions
- Error handling with try/except
- boto3 S3 upload with content-type metadata
- CloudFront cache invalidation via API
- Deployment workflow automation