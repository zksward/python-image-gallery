#!/usr/bin/bash

export IMAGE_GALLERY_SCRIPT_VERSION="1.0"

# Install packages
yum -y update
yum install -y nano python3 git postgresql gcc python3-devel postgresql-devel
amazon-linux-extras install -y nginx1

# Configure/install custom software
cd /home/ec2-user
git clone https://github.com/zksward/python-image-gallery.git
chown -R ec2-user:ec2-user python-image-gallery
su ec2-user -l -c "cd ~/python-image-gallery && pip3 install -r requirements.txt --user"

aws s3 cp s3://${BUCKET_NAME}/nginx/nginx.conf /etc/nginx
aws s3 cp s3://${BUCKET_NAME}/nginx/default.d/image_gallery.conf /etc/nginx/default.d
aws s3 cp s3://${BUCKET_NAME}/nginx/index.html /usr/share/nginx/html
chown nginx:nginx /usr/share/nginx/html/index.html

# Start/enable services
systemctl stop postfix
systemctl disable postfix
systemctl start nginx
systemctl enable nginx

su ec2-user -l -c "cd ~/python-image-gallery && ./serve" >/var/log/image_gallery.log 2>&1 &