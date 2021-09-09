
# Introduction

This is the answer to a proposed challenge. I coded this in my spare time, after did a self-learning crash course about AWS Lambda. That said, there is a plenty of room for improvements.


## Deployment

This project is MAC and Linux compatible, Windows should work(ish?) but could need some CLI adjustements. To deploy this project simply download or clone all files locally and follow the instuctions bellow.

Make sure you have Python 3 installed:
```bash
python3 --version
```
The output should be something similar:
  ```bash
Python 3.8.10
```
You also make sure you have the  modules boto3 and tabulate installed: 
  ```bash
pip list | grep boto3 && pip list | grep tabulate
```
Output expected (versions may vary) :
```bash
boto3                  1.18.31             
tabulate               0.8.9
```
You will also need Terraform 0.12 installed to deploy the AWS Lambda Function as well as the latest AWS CLI to execute the script.
If any requirements are not met, please check the appendix session about how to install Python and the modules needed.

Download all files on the [link](https://github.com/eduardofortes001/assignments) or clone the following Github repository:
```bash
git clone https://github.com/eduardofortes001/assignments
```
Make sure you have AWS credentials with permission to deploy and execute lambda functions, get EC2 information, as well as a IAM role created with these 
permissions.
Check if you have a default AWS profile created with your credentials.
Update the key "role_arn" in the aws_lambda_function.tf file.
Deploy the AWS Lambda Function executing the following commands (It will ask for an AWS region):
```bash
terraform new workspace temporary
terraform init
terraform plan
terraform apply -auto-approve
```
Set the execution permission in the getec2.py script:
```bash
chmod +x getec2.py
```
After the deployment you just need run the script getec2.py.
```bash
./getec2.py
```
It will ask for an Instance id or * which will get all instances available in the region and present the information in a simple table format.

You could also invoke the lambda function directly from CLI but in this case you have to replace instance id in the payload properly either with * or the propper Instance id and look for the response.json file where the command will write the information in a json format.
```bash
aws lambda invoke --cli-binary-format raw-in-base64-out --function-name ec2_Function --payload '{"Instance":"instance_id"}' response.json
```
```bash
cat response.json
```
Enjoy!

## Authors

- [@eduardofortes001](https://github.com/eduardofortes001)

  
## Appendix

 - [Install Python 3](https://www.python.org/downloads/)
 - [Install Packages](https://packaging.python.org/tutorials/installing-packages/)
 - [Install Terraform](https://learn.hashicorp.com/tutorials/terraform/install-cli)
 - [Install AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html)
 - [Creating AWS Profile](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html)
 - [Terraform AWS Lambda module documentation](https://registry.terraform.io/modules/terraform-aws-modules/lambda/aws/latest)
 - [AWS Lambda Developer Guide](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
 - [Using Lambda with AWS CLI](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-awscli.html)
 
 
