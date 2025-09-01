
import os
import glob
import nibabel as nib
import matplotlib.pyplot as plt
import numpy as np
import time

# Define the root directory
root_dir = r'F:\MRA Data\derivatives\N4_bias_field_corrected'
#root_dir = r'F:\Labels\masks'

# Initialize an empty list to store the slices
all_slices = []

# Iterate through all directories and subdirectories using os.walk
for root, _, files in os.walk(root_dir):
    # Check if the directory name starts with "sub-" and contains "ses-" and "anat"
    if root.endswith("anat") and "ses-" in root:
        # List all .nii.gz files within the "anat" directory
        nii_files = glob.glob(os.path.join(root, "*.nii.gz"))
        for nii_file in nii_files:
            # Load and process each .nii.gz file
            nii_img = nib.load(nii_file)
            nii_data = nii_img.get_fdata()
            h, w, shape = nii_data.shape
            for slice_idx in range(shape):
                slice_data = nii_data[:, :, slice_idx]
                # Append the slice to the list
                all_slices.append(slice_data)
                plt.imshow(slice_data, cmap='gray')
                plt.title(f'Slice {slice_idx}')
                plt.axis('off')
                plt.show()
                #print(slice_idx)
            print(f"Processed: {nii_file}")

# Convert the list of slices into a NumPy array
all_slices = np.array(all_slices)

# The shape of all_slices should be (number_of_slices, h, w)
print(all_slices.shape)

# You can add your specific code to process the .nii.gz files inside the loop.
