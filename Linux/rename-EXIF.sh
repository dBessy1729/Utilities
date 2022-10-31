#!/bin/bash

find -name '*.jpg' | while read PIC; do
DATE=$(exiftool -p '$DateTimeOriginal' $PIC |
sed 's/[: ]//g')
touch -t $(echo $DATE | sed 's/\(..$\)/\.\1/') $PIC
mv -i $PIC $(dirname $PIC)/$DATE.jpg
done
