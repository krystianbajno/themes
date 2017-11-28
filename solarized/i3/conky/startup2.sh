#!/bin/sh
kill -s 9 $(pgrep startup.sh)
killall -q conky
conky -q -c /home/krystian/.conky/conky &
route=$(ip route show)
if [[ $route ]];
then
	ipaddress=$(curl ifconfig.pl)
	location=$(geoiplookup $ipaddress)
	whos=$(whois $ipaddress | grep -A 20 inetnum)
	notify-send "Public IP: $ipaddress" -t 5000 
	notify-send "$whos" -t 5000
	notify-send "$location" -t 5000
fi
exit
