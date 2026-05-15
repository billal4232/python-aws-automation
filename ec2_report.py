import boto3
import json
def get_ec2_client():
    session = boto3.Session(profile_name = "limonlab")
    ec2 = session.client("ec2")
    region = session.region_name
    return ec2,region
ec2,region = get_ec2_client()

def get_instances_details(ec2,region):
    try:
        report = []
        # TODO: Add paginator support for large environments
        response = ec2.describe_instances()
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                name = "No Name"
                for tag in instance.get('Tags' ,[]):
                    if tag['Key'] == "Name":
                        name = tag['Value']
                report.append({
                    'instance_id': instance['InstanceId'],
                    'instance_type': instance['InstanceType'],
                    'state': instance['State']['Name'],
                    'name': name,
                    'launch_time': str(instance['LaunchTime']),
                    'region': region
                    })
        return report    
    except Exception as e:
        print(f"Error: {e}")
        return None
    
report = get_instances_details(ec2,region)

def print_report(report):
    for instance in report:
        print(f"Instance ID:  {instance['instance_id']}")
        print(f"Name:         {instance['name']}")
        print(f"State:        {instance['state']}")
        print(f"Type:         {instance['instance_type']}")
        print(f"Launch Time:  {instance['launch_time']}")
        print(f"Region:       {instance['region']}")
        print("---")

if report is not None:    
    with open ("ec2_report.json", "w") as file:
        json.dump(report, file, indent = 4)

    print("Report saved to ec2_report.json")
    print_report(report)
else:
    print("No data to save")




