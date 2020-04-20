FROM debian:stretch

# Follow the cookbook to make the dumpling!
COPY * /srv/

# Set timezone to America/New_York.
RUN ln -sf /usr/share/zoneinfo/America/New_York /etc/localtime

# Install Python development tools, compilers, and build dependencies.
# apt-transport-https is needed for installing nodejs.
# bzip2, tar, wget are needed to download phantomjs.
# default-jre needed for Tabula.
# git is needed to download oaglib.
# gnupg is needed to authenticate the install of nodejs.
# graphviz is needed for dask.dataframe.DataFrame.visualize
# libgeos, and libproj needed for contextily.
# locales is needed to allow for installing Python packages that use unicode
# characters.
# lsb-release is used with nodejs to determine what distro release we're using.
# proj-bin is needed for pyproj.
# unixodbc-dev is needed to build pyodbc.
# GDAL depends on specific versions of its C/C++ libraries, so just
# install the Debian package instead of building from source.

RUN apt-get -qq update
RUN apt-get install -qy --no-install-recommends \
   apt-transport-https \
   bzip2 \
   curl \
   default-jre \
   g++ \
   gcc \
   git \
   gnupg \
   graphviz \
   libffi-dev \
   libgeos-dev \
   libproj-dev \
   locales \
   lsb-release \
   proj-bin \
   proj-data \
   python3-dev \
   python3-gdal \
   python3-pip \
   python3-venv \
   python3-wheel \
   tar \
   unixodbc-dev \
   unzip \
   virtualenv \
   wget

# Set locale to en-US UTF-8
# sets new locale in dpkg to en-US UTF-8 and makes it default
RUN locale-gen en_US.UTF-8 && \
printf "152\n3" | dpkg-reconfigure locales && \
update-locale LANG=en_US.UTF-8 && \
export LANG=en_US.UTF-8

# Install NodeJS for use with Jupyter.
RUN wget --quiet -O - https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add -
RUN wget --quiet -O - https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
# update node_12.x and stretch as stable node version changes
# TODO: potentially automate this?
RUN echo "deb https://deb.nodesource.com/node_12.x stretch main" | tee /etc/apt/sources.list.d/nodesource.list
RUN echo "deb-src https://deb.nodesource.com/node_12.x stretch main" | tee -a /etc/apt/sources.list.d/nodesource.list
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee -a /etc/apt/sources.list.d/nodesource.list
RUN apt-get update && apt-get install -qy --no-install-recommends nodejs yarn

# Create a symlink from python/pip to Python 3,
# since we are not using Python 2.
RUN ln -s ../../bin/python3 /usr/local/bin/python && ln -s ../../bin/pip3 /usr/local/bin/pip

# Python 3.8 needed for black.
RUN apt-get install -qy --no-install-recommends \
    make \
    build-essential \
    libbz2-dev \
    libc6-dev \
    libgdbm-dev \
    libreadline-gplv2-dev \
    libncurses5-dev \
    libncursesw5-dev \
    libsqlite3-dev \
    libssl-dev \
    llvm \
    tk-dev \
    xz-utils \
    zlib1g-dev
# Install pyenv
RUN /srv/pyenv-install.sh

# Step 2 - Pack the dumpling with lots of veggies and steam it.
# Install Python packages for data science.
# setuptools needs to be installed first for cython.
# Cython needs to be installed first for fastparquet, used by dask.
# llvmlite is needed for fastparquet.
# We can remove fastparquet once dask fully supports pyarrow.
RUN grep -v "#" /srv/dumpling_packages.txt > /srv/tmp.txt
RUN mv /srv/tmp.txt /srv/dumpling_packages.txt
RUN pip3 install --no-cache-dir setuptools && \
pip3 install --no-cache-dir cython && \
pip3 install --no-cache-dir -i https://pypi.anaconda.org/sklam/simple llvmlite && \
pip3 install --no-cache-dir -r /srv/dumpling_packages.txt

# TODO: requirements.txt for labextension?
RUN jupyter labextension install @jupyter-widgets/jupyterlab-manager --no-build && \
jupyter labextension install jupyterlab-plotly --no-build && \
jupyter labextension install plotlywidget --no-build && \
jupyter labextension install @jupyterlab/toc && \
jupyter lab build

# Install Chromium as a Selenium WebDriver (replaces PhantomJS).
RUN chmod 770 /srv/chromium-install.sh && /srv/chromium-install.sh


# Orca install steps
RUN npm install --unsafe-perm=true --allow-root -g electron@6.1.4 orca \
   && apt install xvfb -y --no-install-recommends \
   && mv /usr/bin/orca /usr/bin/orca-real \
   && mv /srv/orca /usr/bin/orca \
   && chmod 755 /usr/bin/orca

# Copy lab-asst-dumpling to right location
RUN cp /srv/lab-asst-dumpling /usr/local/bin/lab-asst && chmod 755 /usr/local/bin/lab-asst


# Step 3 - Add some dipping sauce to the dumpling.
# Install Debian packages for convenient CLI work.
# bash-completion, cowsay, fortune* are used in bashrc.
# cifs-utils, gosu are used in docker-entrypoint.
# locales is needed to support UTF-8 locale, which is required by tmux.
RUN apt-get install -qy --no-install-recommends \
   bash-completion \
   bc \
   cifs-utils \
   cookiecutter \
   cowsay \
   curl \
   dnsutils \
   fortune-mod \
   fortunes \
   fortunes-bofh-excuses \
   ghostscript \
   gifsicle \
   gosu \
   host \
   htop \
   imagemagick \
   jq \
   less \
   locales \
   lsof \
   man-db \
   nano \
   net-tools \
   openssh-client \
   p7zip-full \
   postgresql-client \
   procps \
   shellcheck \
   sudo \
   tree \
   tmux \
   vim \
   watch

# Step 4 - Indulge in the dumpling.
# Enable sudo without a password.
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' > /etc/sudoers.d/nopasswd

# Modify bashrc to enable bash-completion and other savories.
# Enable git pull rebase autostash.
# Configure Jupyter Notebook port.
RUN echo '. /srv/bashrc' >> /etc/bash.bashrc
RUN echo '. /srv/bash_logout' >> /etc/bash.bash.logout
RUN ln -s /srv/gitconfig /etc/.
RUN mkdir /etc/jupyter
RUN ln -s /srv/jupyter_notebook_config.py /etc/jupyter/.

# Default to UTF-8 locale.
RUN echo 'en_US.UTF-8 UTF-8' > /etc/locale.gen
RUN locale-gen
RUN update-locale LANG=en_US.UTF-8

# Step 5 - Clean the dishes.
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/*
RUN rm -rf /usr/local/share/.cache
RUN rm -rf /root/.cache

# Serve the chopsticks.
# Use the entrypoint script to add users from host to the container.
ENTRYPOINT ["/srv/docker-entrypoint"]
CMD ["bash"]
