#!/bin/bash
apt-get update
apt-get install -y python
apt-get install -y wget
apt-get install -y wget
pip install requests
wget -O s.py https://raw.githubusercontent.com/SimaKyr/mcs-bedrock/main/s.py
termux-chroot
python s.py