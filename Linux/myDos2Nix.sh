#!/bin/bash

# Accept file name from args, read file
# line by line and strip carriage returns.

FILE=$1

if [ -f $FILE ];
then
  cat $1 | tr -d "\r"
else
  echo "File $FILE does not exist!"
fi
