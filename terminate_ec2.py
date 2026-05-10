import boto3
session = boto3.Session(profile_name = "limonlab", region_name = "eu-north-1")

ec2 = session.client("ec2")

response = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])


instance_ids = []

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        name = ""
        for tag in instance.get('Tags',[]):
            if tag['Key'] == 'Name':
                name = tag['Value']
        print(f"Instance Id: {instance['InstanceId']}, Instance Type: {instance['InstanceType']}, State: {instance['State']['Name']}, Name: {name} ")
        instance_ids.append(instance['InstanceId'])

instance_id = input("Enter the Instance Id you want to terminate: ")

if instance_id in instance_ids:
    confirm = input(f"Are you sure you want to terminate {instance_id}? (yes/no): ")

    if confirm == "yes":
       response = ec2.terminate_instances(InstanceIds=[instance_id])
       print("Terminated")
    else:
        print("Cancelled")
else:
    print("No valid id is found")
