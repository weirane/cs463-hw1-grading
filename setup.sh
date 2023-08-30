#!/bin/sh

apt-get update
apt-get install -y build-essential python3 python3-pip python3-dev

cd /autograder/source || exit 1
pip3 install -r requirements.txt
