import boto3

# Connect to AWS using limonlab profile and eu-north-1 region
session = boto3.Session(profile_name='limonlab', region_name='eu-north-1')

# Create EC2 client to interact with EC2 service
ec2 = session.client('ec2')

# Get all EC2 instances from AWS
response = ec2.describe_instances()

# Ask user which instance they want to terminate
search_name = input("Type instance name to terminate: ")

# Assume no match found yet
found = False

# Loop through AWS response structure to reach each instance
for reservation in response['Reservations']:
    for instance in reservation['Instances']:

        # Get Name tag safely — returns empty list if no tags exist
        name = ''
        for tag in instance.get('Tags', []):
            if tag['Key'] == 'Name':
                name = tag['Value']

        # Check if this instance matches the name user typed
        if name == search_name:
            print(f"Found: {instance['InstanceId']} — {name}")

            # Ask for confirmation before terminating
            confirm = input("Are you sure you want to terminate? (yes/no): ")
            if confirm == "yes":
                ec2.terminate_instances(InstanceIds=[instance['InstanceId']])
                print("Terminated.")
                found = True
            else:
                print("Cancelled.")
                found = True

# If no instance matched the name typed
if not found:
    print("No instance found with that name.")