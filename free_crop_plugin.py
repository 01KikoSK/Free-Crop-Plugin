#!/usr/bin/env python

from gimpfu import *

def free_crop(image, drawable):
    # Start undo group
    pdb.gimp_image_undo_group_start(image)
    
    # Get the current selection bounds
    non_empty, x1, y1, x2, y2 = pdb.gimp_selection_bounds(image)
    
    if non_empty:
        # Crop the image to the selection
        pdb.gimp_image_crop(image, x2 - x1, y2 - y1, x1, y1)
    else:
        pdb.gimp_message("No selection found. Please make a freehand selection first.")
    
    # End undo group
    pdb.gimp_image_undo_group_end(image)
    pdb.gimp_displays_flush()

register(
    "python_fu_free_crop",
    "Free Crop",
    "Crop the image to a freehand selection",
    "Your Name",
    "Your Name",
    "2025",
    "<Image>/Tools/Transform Tools/Free Crop...",
    "*",
    [],
    [],
    free_crop)

main()