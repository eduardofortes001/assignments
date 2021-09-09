provider "aws" {
  profile = "default"
}

module lambda {
  source  = "terraform-module/lambda/aws"
  version = "2.12.6"

  function_name      = "ec2_Function"
  filename           = "ec2_Function.zip"
  description        = "This AWS Lambda function retrieves basic information about EC2 instances including disk size."
  handler            = "ec2_Function.lambda_handler"
  runtime            = "python3.8"
  memory_size        = "128"
  concurrency        = "5"
  lambda_timeout     = "60"
  log_retention      = "1"
  role_arn           = "arn:aws:iam::655770298923:role/service-role/cocus-role-0459zoay"

}
