import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def list_s3_buckets():
    try:
        s3 = boto3.client('s3')
        response = s3.list_buckets()
        
        print("S3 Buckets:")
        for bucket in response['Buckets']:
            print(f"- {bucket['Name']}")
    except (NoCredentialsError, PartialCredentialsError):
        print("AWS credentials not found or incomplete.")
    except Exception as e:
        print(f"An error occurred: {e}")

def list_ec2_instances():
    try:
        ec2 = boto3.client('ec2')
        response = ec2.describe_instances()
        
        print("EC2 Instances:")
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                print(f"- ID: {instance['InstanceId']}, State: {instance['State']['Name']}")
    except (NoCredentialsError, PartialCredentialsError):
        print("AWS credentials not found or incomplete.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    print("AWS Resource Manager")
    print("1. List S3 Buckets")
    print("2. List EC2 Instances")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        list_s3_buckets()
    elif choice == "2":
        list_ec2_instances()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
