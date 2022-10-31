#!/bin/bash

find ~/working/temp/backups -type f -iname 'syslog.*' -mtime +28 -exec ls -l {} +
