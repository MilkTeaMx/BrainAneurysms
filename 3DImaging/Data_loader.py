from torch.utils.data import Dataset, DataLoader
from torchvision import transforms
from PIL import Image
import os

#NEEDS IMAGES - 4th
class CustomDataset(Dataset):
    def __init__(self, image_dir, mask_dir, transform=None):
        self.images = sorted(os.listdir(image_dir))  # Assuming images are in the image_dir
        self.masks = sorted(os.listdir(mask_dir))  # Assuming masks are in the mask_dir
        self.image_dir = image_dir
        self.mask_dir = mask_dir
        self.transform = transform

    def __len__(self):
        return len(self.images)

    def __getitem__(self, idx):
        img_path = os.path.join(self.image_dir, self.images[idx])
        mask_path = os.path.join(self.mask_dir, self.masks[idx])
        
        image = Image.open(img_path)
        mask = Image.open(mask_path)
        
        if self.transform:
            image = self.transform(image)
            mask = self.transform(mask)

        return {'image': image, 'mask': mask}


image_dir = "F:\\Train\\train-images\\"
mask_dir = "F:\\Train\\train-masks\\"

# Define the transformations
trans = transforms.Compose([
    transforms.Grayscale(num_output_channels=1),
    transforms.ToTensor(),
    transforms.Normalize([0.485], [0.229]) # mean and std for a single channel
])


# Load the datasets
train_set = CustomDataset(image_dir, mask_dir)
val_set = CustomDataset(image_dir, mask_dir)

# Rest of the code remains the same
image_datasets = {'train': train_set, 'val': val_set}
batch_size = 25
dataloaders = {'train': DataLoader(train_set, batch_size=batch_size, shuffle=True, num_workers=0),
               'val': DataLoader(val_set, batch_size=batch_size, shuffle=True, num_workers=0)}
print(len(train_set))

import matplotlib.pyplot as plt
import numpy as np

# Create an iterator for the DataLoader
train_loader = iter(dataloaders['train'])

# Fetch a batch of data
data = train_loader.next()

# Get the images and masks from the batch
images, masks = data['image'], data['mask']

# Convert the tensors to numpy arrays for visualization
np_images = images.numpy()
np_masks = masks.numpy()

# Plot the images from the batch
fig, axes = plt.subplots(5, 5, figsize=(15, 15))
for i, ax in enumerate(axes.flat):
    # Convert the tensor to a numpy array
    np_image = np.transpose(np_images[i], (1, 2, 0))
    np_mask = np.transpose(np_masks[i], (1, 2, 0))

    ax.imshow(np_image)
    ax.imshow(np_mask, alpha=0.3)
    ax.axis('off')

plt.show()
