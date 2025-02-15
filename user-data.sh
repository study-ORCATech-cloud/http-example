Content-Type: multipart/mixed; boundary="//"
MIME-Version: 1.0

--//
Content-Type: text/cloud-config; charset="us-ascii"
MIME-Version: 1.0
Content-Transfer-Encoding: 7bit
Content-Disposition: attachment; filename="cloud-config.txt"

#cloud-config
cloud_final_modules:
- [scripts-user, always]

--//
Content-Type: text/x-shellscript; charset="us-ascii"
MIME-Version: 1.0
Content-Transfer-Encoding: 7bit
Content-Disposition: attachment; filename="userdata.txt"

#!/bin/bash

# set environment variables
export HOME=/home/ec2-user

mkdir -p ${WORKDIR} | true

# initial instance installations
if [ ! -f .env.${ENV} ]; then
    yum update -y
    yum install docker-25.0.6-1.amzn2023.0.1 -y

    # curl -L "https://github.com/docker/compose/releases/download/v2.19.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    # chmod +x /usr/local/bin/docker-compose

    systemctl start docker
fi

secret_sm=$(aws secretsmanager get-secret-value --secret-id ${ENV}/${APP_NAME}/env --query SecretString --output text)
secret_ssm=$(aws ssm get-parameter --name /dev/chokomoko/secret --query "Parameter.Value" --output text)


docker run --rm -d -p 5000:5000 -e CHOKOMOKO_SECRET_SM=${secret_sm} -e CHOKOMOKO_SECRET_SSM=${secret_ssm} orcatechwork/http-example:1.2.0
--//--