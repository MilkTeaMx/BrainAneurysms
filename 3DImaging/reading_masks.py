# import os
# import glob
# import nibabel as nib
# import matplotlib.pyplot as plt
# import numpy as np

# # Define the root directory
# root_dir = r'F:\MRA Data\derivatives\manual_masks'
# output_dir = r'F:\MRA-Images'  # Specify the output directory

# # Iterate through all directories and subdirectories using os.walk
# for root, _, files in os.walk(root_dir):
#     # Check if the directory name starts with "sub-" and contains "ses-" and "anat"
#     if root.endswith("anat") and "ses-" in root:
#         # Extract session name from the path
#         session_name = os.path.basename(os.path.dirname(root))
#         # Create a directory in the output path with the session name
#         session_output_dir = os.path.join(output_dir, session_name)
#         os.makedirs(session_output_dir, exist_ok=True)
        
#         # List all .nii.gz files within the "anat" directory
#         nii_files = glob.glob(os.path.join(root, "*.nii.gz"))
#         for nii_file in nii_files:
#             # Load and process each .nii.gz file
#             nii_img = nib.load(nii_file)
#             nii_data = nii_img.get_fdata()
#             h, w, shape = nii_data.shape
#             for slice_idx in range(shape):
#                 slice_data = nii_data[:, :, slice_idx]
#                 # Save the slice as a PNG image
#                 output_path = os.path.join(session_output_dir, f"{session_name}_{slice_idx + 1}.png")  # Adjust slice_idx by 1
#                 plt.imsave(output_path, slice_data, cmap='gray')
#                 # Visualize the slice if needed
#                 #plt.imshow(slice_data, cmap='gray')
#                 #plt.title(f'Slice {slice_idx}')
#                 #plt.axis('off')
#                 #plt.show()
#                 #print(slice_idx)
#             print(f"Processed: {nii_file}")

# # Optionally, you can convert the list of slices into a NumPy array
# # all_slices = np.array(all_slices)

# # Optionally, print the shape of all_slices
# # print(all_slices.shape)

import os# import os
# import glob
# import nibabel as nib
# import matplotlib.pyplot as plt
# import numpy as np

# # Define the root directory
# root_dir = r'F:\MRA Data\derivatives\manual_masks'
# output_dir = r'F:\MRA-Images'  # Specify the output directory

# # Iterate through all directories and subdirectories using os.walk
# for root, _, files in os.walk(root_dir):
#     # Check if the directory name starts with "sub-" and contains "ses-" and "anat"
#     if root.endswith("anat") and "ses-" in root:
#         # Extract session name from the path
#         session_name = os.path.basename(os.path.dirname(root))
#         # Create a directory in the output path with the session name
#         session_output_dir = os.path.join(output_dir, session_name)
#         os.makedirs(session_output_dir, exist_ok=True)
        
#         # List all .nii.gz files within the "anat" directory
#         nii_files = glob.glob(os.path.join(root, "*.nii.gz"))
#         for nii_file in nii_files:
#             # Load and process each .nii.gz file
#             nii_img = nib.load(nii_file)
#             nii_data = nii_img.get_fdata()
#             h, w, shape = nii_data.shape
#             for slice_idx in range(shape):
#                 slice_data = nii_data[:, :, slice_idx]
#                 # Save the slice as a PNG image
#                 output_path = os.path.join(session_output_dir, f"{session_name}_{slice_idx + 1}.png")  # Adjust slice_idx by 1
#                 plt.imsave(output_path, slice_data, cmap='gray')
#                 # Visualize the slice if needed
#                 #plt.imshow(slice_data, cmap='gray')
#                 #plt.title(f'Slice {slice_idx}')
#                 #plt.axis('off')
#                 #plt.show()
#                 #print(slice_idx)
#             print(f"Processed: {nii_file}")

# # Optionally, you can convert the list of slices into a NumPy array
# # all_slices = np.array(all_slices)

# # Optionally, print the shape of all_slices
# # print(all_slices.shape)

import os
import glob
import nibabel as nib
import matplotlib.pyplot as plt
import time


# Define the root directory for masks
root_dir = 'data/data2/trainannot'
output_dir = 'masks'


# Get the list of names from the "F:\MRA-Images\Images\" directory
names_list = []
images_dir = r'F:\MRA-Images\Images'


for dirpath, dirnames, filenames in os.walk(images_dir):
    for dirname in dirnames:
        print(dirname)
        names_list.append(dirname)

# Iterate through all directories and subdirectories using os.walk
for root, _, files in os.walk(root_dir):
    str_file = str(files)
    #time.sleep(10)
    for name in names_list:
        #print(name)
        #time.sleep(2)
        if name in str_file:
            session_name = name
            print(session_name)
            session_output_dir = os.path.join(output_dir, session_name)
            #os.makedirs(session_output_dir, exist_ok=True)
            nii_files = glob.glob(os.path.join(root, "*.nii.gz"))
            str_nii_files = str(nii_files)
            for i in nii_files:
                if session_name in i:
                    #print(i)
                    #time.sleep(4)
                    os.makedirs(session_output_dir, exist_ok=True)
                    nii_img = nib.load(i)
                    nii_data = nii_img.get_fdata()
                    h, w, shape = nii_data.shape
                    for slice_idx in range(shape):
                        slice_data = nii_data[:, :, slice_idx]
                        output_path = os.path.join(session_output_dir, f"{session_name}_{slice_idx + 1}.png")  # Adjust slice_idx by 1
                        plt.imsave(output_path, slice_data, cmap='gray')
                        # Visualize the slice if needed
                        #plt.imshow(slice_data, cmap='gray')
                        #plt.title(f'Slice {slice_idx}')
                        #plt.axis('off')
                        #plt.show()
                        # print(slice_idx)
                    #print(f"Processed: {nii_file}")
                print("Saved to:", session_output_dir)
