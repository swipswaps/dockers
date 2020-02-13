#!/bin/bash
apt-get install -qy --no-install-recommends chromium
apt list chromium -a | grep installed | cut -d ' ' -f2 | cut -d '~' -f1
# determine closest version number
installed_version=$(apt list chromium -a | grep installed | cut -d ' ' -f2 | cut -d '~' -f1 | cut -d "." -f1,2,3)
version=$(curl "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$installed_version")
wget --no-verbose -O chromedriver_linux64.zip "https://chromedriver.storage.googleapis.com/$version/chromedriver_linux64.zip"
unzip chromedriver_linux64.zip
echo "Moving chromedriver to /usr/local/bin"
mv chromedriver /usr/local/bin
echo "Changing chromedriver permissions"
chmod 755 /usr/local/bin/chromedriver
echo "Deleting chromedriver zip"
rm chromedriver_linux64.zip
command -v chromedriver
