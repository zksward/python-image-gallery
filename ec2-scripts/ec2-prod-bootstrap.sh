#!/bin/bash

export IMAGE_GALLERY_BOOTSTRAP_VERSION="1.0"
export BUCKET_NAME="edu.auburn.smw0036.image-gallery-config"

aws s3 cp s3://${BUCKET_NAME}/ec2-prod-latest.sh ./
/usr/bin/bash ec2-prod-latest.sh