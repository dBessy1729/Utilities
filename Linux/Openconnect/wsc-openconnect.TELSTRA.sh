#!/bin/bash

# Connects to the STR GW. Requires STRICN creds.
##sudo openconnect 193.116.26.60 -u jschmitt -g WSC-Anyconnect --no-cert-check
#sudo openconnect 193.116.26.60 -u jschmitt -g WSC-Anyconnect

# This group authenticates using CENTRES domain
sudo openconnect 193.116.26.60 -u jschmitt --authgroup WSC-Anyconnect

