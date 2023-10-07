#!/bin/sh
# xrandr --output DP-1 --primary --mode 3840x2160 --pos 0x1296 --rotate normal --output HDMI-1  --scale 1.20x1.20 --rate 60 --mode 1920x1080 --pos 898x0 --rotate normal --output DVI-D-1 --off &
xrandr --output DP-1 --primary --mode 3840x2160 --pos 0x0 --rotate normal --output HDMI-1 --off --output DVI-D-1 --off
wal -R &
setxkbmap latam &
playerctld daemon &
picom &

