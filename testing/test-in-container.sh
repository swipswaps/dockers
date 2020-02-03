#!/bin/bash

set -euxo pipefail

# check upgrading
sudo apt-get update -y
sudo apt-get upgrade -y

# test black
black .

# install pytest
pip install pytest

# install contextily
sudo apt-get install -y libgeos-dev \
    libproj-dev \
    proj-data \
    proj-bin

pip install contextily

# run pytest
pytest
