#!/bin/bash
IFS=$'\n'

wallpapers_dir="/home/nivalderramas/.config/qtile/wallpapers/"

if [ "$*" = "quit" ]
then
    exit 0
fi

# An option was passed, so let's check it
if [ "$@" ]
then
    selection="$*"
    out=$(wal -i "$wallpapers_dir/$selection" && pywalfox update && qtile cmd-obj -o cmd -f reload_config)
    exit 0
else
    echo -en "\x00prompt\x1fSelect a Wallpaper\n"
    # Get the list of outputs based on the description, which is what makes sense to a human
    # and is what we want to show in the menu
    for x in $(ls "$wallpapers_dir")
    do
        # outputs with cut may have spaces, so use empty xargs to remove them, and output that to the rofi list
        echo "$x" | xargs
    done
    echo "quit"
fi

