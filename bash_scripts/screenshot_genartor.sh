#!/bin/bash

# Launch IGV with the desired region
igv -g hg38 -l $1:$2-$3 &

# Wait for a few seconds to allow the view to load
sleep 15

# Bring the IGV window to the front and ensure that it is in focus
#xdotool search --name "IGV" | xdotool windowactivate --sync

# Capture the screenshot
gnome-screenshot -f screenshot_$1_$2_$3.png

# Kill the IGV process
pkill igv

