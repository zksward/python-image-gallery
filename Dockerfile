FROM ubuntu:latest

# Environment Variables
ARG DEBIAN_FRONTEND=noninteractive
ARG TZ=America/New_York

# Update packages and install
RUN apt-get update && apt-get install -y \
    git \
    libpq-dev \
    python3 \
    python3-pip

# Create User and Group
RUN groupadd -g 32767 imagegallery && useradd --no-log-init -m -u 32767 -g imagegallery imagegallery

# Switch to user
USER imagegallery

WORKDIR /home/imagegallery

# COPY --chown=imagegallery:imagegallery . .
RUN git clone https://github.com/zksward/python-image-gallery.git

WORKDIR /home/imagegallery/python-image-gallery

# Install python dependencies and add to path
RUN pip3 install -r requirements.txt --user

ENV PATH="~/.local/bin:${PATH}"

EXPOSE 8888

# Startup
ENTRYPOINT ["./serve"]
CMD ["/usr/bin/bash"]