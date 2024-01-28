Auto Scaling Group Monitoring with AWS Lambda and Terraform
Overview
This project sets up an AWS infrastructure for monitoring EC2 instances within an Auto Scaling Group using AWS Lambda. The Lambda functions collect historical and just-in-time metrics via CloudWatch API calls.

Architecture
The architecture consists of the following components:

Auto Scaling Group (ASG): Manages EC2 instances dynamically based on demand.
AWS Lambda Functions:
One Lambda function for monitoring EC2 instances and publishing metrics to CloudWatch.
Another Lambda function for retrieving historical and just-in-time metrics via API calls.
Amazon CloudWatch: Stores monitoring metrics.
Prerequisites
AWS Account: Ensure you have an AWS account with the necessary permissions.
Terraform: Install Terraform on your local machine.
Terraform Setup
Clone the repository:

git clone https://github.com/arielzinger38/submittion/
Change into the project directory:

cd autoscaling-monitoring
Initialize Terraform:

terraform init
Create a Terraform execution plan:

terraform plan
Apply the Terraform configuration:

terraform apply
Confirm with yes when prompted.

Running the Lambda Functions
CloudWatch Metric Publishing Function: scaling-monitor
Runs every 2 hours and publishes metrics to cloudwatch

Open the AWS Lambda console.
Locate the function named metrics-api.
Test the function by configuring a new test event. Modify the event payload with the instance ID of your EC2 instance.
Execute the test event to trigger the function and retrieve historical and just-in-time metrics.

Cleanup
To avoid incurring unnecessary costs, remember to destroy the resources created by Terraform when you are done:

terraform destroy
Confirm with yes when prompted.

NOTE i have added the autoscaling Target Tracking Policy manually in the console after running the terraform apply
