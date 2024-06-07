#!/bin/bash

# Launch IGV with the desired region
igv -g hg38 -l chr17:7666085-7666244 &

# Wait for a few seconds to allow the view to load
sleep 6

# Bring the IGV window to the front and ensure that it is in focus
#xdotool search --name "IGV" | xdotool windowactivate --sync

# Capture the screenshot
gnome-screenshot -f screenshot.png

# Kill the IGV process
pkill igv

