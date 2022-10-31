#!/bin/bash

#sudo -i
#cd /home/jim/bin

# Create the tap0 loopback
sudo modprobe tun
sudo tunctl

# Configure IP settings
sudo ifconfig tap0 10.100.100.10 netmask 255.255.255.0 up

# If more than one loopback is needed
# rerun the 'tunctl' command then
# ifconfig tap1 10.101.101.10 netmask 255.255.255.0 up

# Verify success
ifconfig
