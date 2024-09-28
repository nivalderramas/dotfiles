#!/bin/bash

# Function to get the application name
get_app_name() {
    local window_id=$1
    # Use xprop to get the WM_NAME property
    xprop -id $window_id | grep '^WM_NAME(STRING)' | cut -d'"' -f2
}

# Get all visible windows
for window in $(xdotool search --onlyvisible --name .); do
    # Get and print the application name of each window
    app_name=$(get_app_name $window)
    echo "Window ID: $window, Application Name: $app_name"
done

