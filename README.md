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


Copy code
git clone https://github.com/arielzinger38/submittion/
Change into the project directory:


Copy code
cd autoscaling-monitoring
Initialize Terraform:


Copy code
terraform init
Create a Terraform execution plan:


Copy code
terraform plan
Apply the Terraform configuration:


Copy code
terraform apply
Confirm with yes when prompted.

Running the Lambda Functions
CloudWatch Metric Publishing Function:

Open the AWS Lambda console.
Locate the function named AutoScalingMetricsPublisher.
Test the function by configuring a new test event. Modify the event payload as needed.
Execute the test event to trigger the function and publish metrics to CloudWatch.
Metric Retrieval Function:

Open the AWS Lambda console.
Locate the function named AutoScalingMetricRetrieval.
Test the function by configuring a new test event. Modify the event payload with the instance ID of your EC2 instance.
Execute the test event to trigger the function and retrieve historical and just-in-time metrics.
Cleanup
To avoid incurring unnecessary costs, remember to destroy the resources created by Terraform when you are done:

Copy code
terraform destroy
Confirm with yes when prompted.


