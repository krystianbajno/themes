#!/bin/sh
kill -s 9 $(pgrep startup2.sh)
killall -q conky
feh --bg-scale /home/krystian/.config/backgrounds/static/fluv.png
#feh  -z --bg-scale /home/krystian/.config/backgrounds/
#conky -q -c /home/krystian/.conky/conky & conkyid=$!
#sleep 10
#kill -s 15 $conkyid
exit
