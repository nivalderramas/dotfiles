#!/bin/sh
#  xrandr --output DisplayPort-0 --primary --mode 3840x2160 --pos 0x1300 --rotate normal --output HDMI-A-0  --scale 1.30x1.30 --rate 60 --mode 1920x1080 --pos 898x0 --rotate right --output DVI-D-1 --off &
# # xrandr --output DP-1 --primary --mode 3840x2160 --pos 0x0 --rotate normal --output HDMI-1 --off --output DVI-D-1 --off
setxkbmap latam &
playerctld daemon &
picom &
wal -R &
dunst &
