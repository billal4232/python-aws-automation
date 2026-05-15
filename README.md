# python-aws-automation

Python scripts for automating AWS infrastructure tasks using boto3.

## Scripts

### terminate_ec2.py
Lists running EC2 instances and terminates a selected one safely.

**Features:**
- Lists instances with ID, type, state, and name tag
- Confirmation prompt before terminating
- Handles missing tags safely

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
python3 terminate_ec2.py
python3 ec2_report.py
```

## IAM Permissions Required
- ec2:DescribeInstances
- ec2:TerminateInstances

## What I Learned
- AWS response structure — nested Reservations and Instances
- Extracting name from Tags list using loop and condition
- Dynamic region detection from AWS config
- Separating concerns using functions
- Error handling with try/except per function