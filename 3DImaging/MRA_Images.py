#==================================
import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt
#==================================
# load image (4D) [X,Y,Z_slice,time]


#THIS FILE SHOWS IMAGES OF EACH 4D IMAGE


nii_img  = nib.load('data2/train/sub-000_ses-20110101_desc-brain_mask.nii.gz')
print(nii_img.shape)
nii_data = nii_img.get_fdata()
h, w, shape = nii_data.shape

for slice_idx in range(shape):
    slice_data = nii_data[:, :, slice_idx]
    plt.imshow(slice_data, cmap='gray')
    plt.title(f'Slice {slice_idx}')
    plt.axis('off')
    plt.show()