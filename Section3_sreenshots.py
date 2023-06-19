import os
import streamlit as st
from PIL import Image
import numpy as np

# Define the path to the folder containing the images
path = "C:/Users/matan.s/Pictures/section 3"

# # Get a list of all the image files in the folder
image_files = [os.path.join(path, f) for f in os.listdir(path) if f.endswith(".jpg") or f.endswith(".png")]
print(image_files)

# # Display the images in a 4x4 grid
st.set_page_config(page_title="Image Viewer")
st.title("Image Viewer")

# num_images = len(image_files)
# num_rows = 4
# num_cols = int(np.ceil(num_images / num_rows))

for i in range(len(image_files)):
    #make this as a 4iun a row grid
    image = Image.open(image_files[i])
    st.header(i)
    #place the numerators in the grid
    st.image(image, caption=i, use_column_width=True)
    #write the number i below the image
    
    

