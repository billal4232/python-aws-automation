# python-aws-automation

Python scripts for automating AWS infrastructure tasks using boto3.

## Scripts

### terminate_ec2.py

Searches for an EC2 instance by Name tag and terminates it safely.

**Features:**
- Lists and searches instances by Name tag
- Confirmation prompt before terminating
- Handles missing tags safely
- Clear error message if instance name not found

**Example:**
```
Type instance name to terminate: web-server
Found: i-0abc123 — web-server
Are you sure you want to terminate? (yes/no): yes
Terminated.
```

## Requirements

- Python 3
- boto3 installed
- AWS CLI configured with appropriate profile

## Setup

```
pip install boto3 --break-system-packages
python3 terminate_ec2.py
```

## What I Learned

- AWS response structure — nested dictionaries and lists
- Safely accessing dictionary keys with `.get()` to handle missing tags
- Using boto3 Session with named profiles
- Building safe automation with confirmation prompts before destructive actions
