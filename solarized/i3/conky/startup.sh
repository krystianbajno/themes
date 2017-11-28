#!/bin/sh
kill -s 9 $(pgrep startup2.sh)
killall -q conky
exit
