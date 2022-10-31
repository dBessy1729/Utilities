#!/bin/bash

#echo -n "Enter a base device name -> "
#read var1

#echo -n "Enter the amount of devices-> "
#read var2

NAME=$1
START=1
END=$2

if [[ "$2" =~ ^[1-9]+$ ]]; then
	for i in $(seq $START $END)
		do
			echo "$NAME$i"
		done
else
	echo "$2 is not an integer." >&2
	exit 1
fi

