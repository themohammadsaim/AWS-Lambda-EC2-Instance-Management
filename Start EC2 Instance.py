#Lambda Function to Start an EC2 Instance 
#This script is a Lambda function that starts an EC2 instance. It initializes an EC2 client, connects to the specified AWS region, and then starts the EC2 instance identified by its instance ID.  Ensure to replace the placeholders `<your-region>` and `<your-instance-id>` with the actual region and instance ID for your EC2 instance.

# To Start an EC2 Instance
import boto3

def lambda_handler(event, context):
    # Initialize the EC2 client
    ec2_client = boto3.client('ec2', region_name='<your-region>')  # Replace <your-region> with your AWS region
    
    # Specify the instance ID of the EC2 instance you want to start
    instance_id = '<your-instance-id>'  # Replace <your-instance-id> with your EC2 Instance ID

    # Start the EC2 instance
    try:
        response = ec2_client.start_instances(InstanceIds=[instance_id], DryRun=False)
        print(f"Starting EC2 instance {instance_id}...")
        print(f"Response: {response}")

        return {
            'statusCode': 200,
            'body': f"EC2 instance {instance_id} is being started."
        }

    except Exception as e:
        print(f"Error starting EC2 instance: {e}")
        return {
            'statusCode': 500,
            'body': f"Error starting EC2 instance: {str(e)}"
        }
