#!/bin/sh
feh --bg-scale /home/krystian/.config/backgrounds/static/fluv.png
kill -s 9 $(pgrep startup.sh)
killall -q conky
conky -q -c /home/krystian/.conky/conky &
exit
