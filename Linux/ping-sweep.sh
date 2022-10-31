#!/bin/bash

# ping-sweep : ping a range of IP addresses

is_alive_ping()
{
	ping -c 1 $1 > /dev/null
	[ $? -eq 0 ] && echo Node with IP: $i is up.
}

echo $(date)

for i in 192.168.1.{1..254}; do
	is_alive_ping $i & disown
done

echo $(date)
