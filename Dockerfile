# DOCKER HUB LINK: https://hub.docker.com/r/smw0036/image-gallery-smw0036

FROM ubuntu:latest

# Environment Variables
ARG DEBIAN_FRONTEND=noninteractive
ARG TZ=America/New_York
ENV PG_HOST=ec2-18-188-184-252.us-east-2.compute.amazonaws.com
ENV PG_PORT=5432
ENV IG_DATABASE=imagegallery
ENV IG_USER=imagegallery
ENV IG_PASSWD=smw0036
ENV IG_PASSWD_FILE=
ENV FLASK_SECRET_KEY=buHppx66xaEzXgyqk4VsX5UqMch4YFYB
ENV S3_IMAGE_BUCKET=edu.auburn.smw0036.image-gallery

# Update packages and install
RUN apt-get update && apt-get install -y \
    git \
    libpq-dev \
    postgresql \
    python3 \
    python3-pip

# Create User and Group
RUN groupadd -g 32767 imagegallery && useradd --no-log-init -m -u 32767 -g imagegallery imagegallery

# Switch to user
USER imagegallery

# Install python dependencies and add to path
COPY --chown=imagegallery:imagegallery requirements.txt /app/
WORKDIR /app
RUN pip3 install -r requirements.txt --user
ENV PATH="~/.local/bin:${PATH}"

# Copy app files
COPY --chown=imagegallery:imagegallery . /app/

EXPOSE 8888

# Startup
CMD ["/bin/bash", "/app/serve"]