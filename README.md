# MoviesRecommendationSystemMLops


# Procedure of Creating a Environment

<!-- pip install virtualenv (if not installed)

virtualenv mrs_env  # Replace "mrs_env" with the name you want for your environment -->


# environment = mrs_env
# Activate the env by pasting this on gitbash => source mrs_env/Scripts/activate 

URI -> 625374339876.dkr.ecr.us-east-1.amazonaws.com/mrs
Access key ID = AKIAZDGZXEMSEUTBTGXV
Secret access key = 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

s3://my-mrs-bucket/artifacts/model_trainer/movies.joblib [As i have uploaded my two files in these dirs(/artifacts/model_trainer/movies.joblib && /artifacts/model_trainer/similarity.joblib) ]

## Problem Statement
I ENABLED THE CI-CD pipeline using github actions and how i handle the large file issue as the model file was over 100 MB and for a streamlit application it requires the modelfile so during deployment , it was asking the files which are  present as artifacts/model_trainer/movies.joblib and we just ignore the artifacts folder as we dont push the file in our github repo. Now the problem arises that if we don't have the access then how will the model perform so now AWS S3 bucket comes  in the picture and just best solution to this problem was that to just upload the files to s3 bucker and then download it in the aws ec2 instance and then only the deployment engine gets the file what it want. So the steps how i did this are as follows -: 

Step-1 -: We just create the IAM user and we will keep the id and security key credentials and we will keep certain 
          policies which are - AmazonEC2ContainerRegistryFullAccess
                             - AmazonEC2FullAccess
                             - AmazonS3FullAccess
                             - AmazonS3ReadOnlyAccess
Step-2 -: We will create the ECR repo inorder to push the docker image and here we will keep the uri id
Step-3 -: We will create the EC2 instance with proper requirement what the project wants.
Step-4 -: We will Connect the EC2 instance using CLI
Step-5 -: Now we will input certain commands like -:
            #optinal

            sudo apt-get update -y

            sudo apt-get upgrade

            #required

            curl -fsSL https://get.docker.com -o get-docker.sh

            sudo sh get-docker.sh

            sudo usermod -aG docker ubuntu

            newgrp docker
Step-6 -: We will open the github repo and then go on the tab of settings/actions/and we will again input all the commands of git in aws-CLI and then our repo will get connected with aws

Step-7 -: We will created Dockerfile and .github/main.yaml and we will enter the codes as for Flask app and         Streamlit app has diffrent codes for both files [small-changes] 

Step-8 -: Now will push the changes to the github and then we will see the logs of CI-CD pipeline in github/actions

Step-9 -: Now we have the .pem file that we downloaded when we were creating ec2 instance. We will convert this file
          to .ppk via PuttYgen software as we just open the Puttygen &
          Conversions/Import key/Save Private Key

Step-10 -: Now we will open Putty and give the input for the IP-address that we get in AWS ec2 - [the-public-ip-add]
           the Go to SSH/Auth/Credentials and we will browse the Private key and Open

Step-11 -: We will now input the login as -: ubuntu and you will be connected to to your repo but ur repo has only two files like -: ubuntu@ip-172-31-18-142:~$ ls
                  actions-runner  get-docker.sh
                  ubuntu@ip-172-31-18-142:~$

Inorder to access the files of repo we will input some command -:

docker ps [Note the 'name' of the container]
docker exec -it <container-id-or-name> /bin/bash
ls

And here are files -: of repo
now will install
                - apt-get update
                - apt-get install -y nano

nano file1.py -: "This file will download the first file and u can create as many file as you want for download from S3"

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 

import boto3

aws_access_key_id = 'AKIAZDGZXEMSJ2BY4ULY'
aws_secret_access_key = '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'
bucket_name = 'my-mrs-bucket'
file_key = 'artifacts/model_trainer/similarity.joblib'

# Create an S3 client
s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

# Specify the local file path where you want to save the downloaded file
local_file_path = 'artifacts/model_trainer/similarity.joblib'

# Download the file
s3.download_file(bucket_name, file_key, local_file_path)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For file_key = 'artifacts/model_trainer/similarity.joblib' coz i have uploaded the files in such a way by making the dirs inside S3

For local_file_path = 'artifacts/model_trainer/similarity.joblib' as it will be downloaded at this path only.
                       and make sure your ec2 has artifacts/model_trainer folders are present or else you have to create [it is based on your project]


Step-12-: Now we will check whether the files are present or not and then we will run both files
          python3 file1.py
          and then we will check whether the file is downloaded or not

Step-13-: we will then input exit and we will roll back

Step-14-: We will go to AWS EC2 and we will go and include the custom TCP port of 8501
          [Compulsory-for-streamlit-apps]
Step-15-: Now, just copy the public address with the port number and the application should run.





