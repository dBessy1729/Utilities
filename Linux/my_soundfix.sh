#!/bin/bash
#
# Workaround for sound problem at startup which has happened since 
# upgrade to Ubuntu 18.10.
#
# Might be worth running the script at login but manual for now.

sudo alsa force-reload
