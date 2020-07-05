FROM ubuntu:latest

# Environment Variables
ARG DEBIAN_FRONTEND=noninteractive
ARG TZ=America/New_York
ENV PG_HOST=192.168.1.16
ENV PG_PORT=5432
ENV IG_DATABASE=imagegallery
ENV IG_USER=imagegallery
ENV IG_PASSWD=smw0036
ENV IG_PASSWD_FILE=
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

# Copy app files
COPY --chown=imagegallery:imagegallery . /app/

WORKDIR /app

# Install python dependencies and add to path
RUN pip3 install -r requirements.txt --user

ENV PATH="~/.local/bin:${PATH}"

EXPOSE 8888

# Startup
#ENTRYPOINT ["./serve"]
CMD ["/bin/bash"]