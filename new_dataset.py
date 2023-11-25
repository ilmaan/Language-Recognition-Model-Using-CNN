import os
import shutil
from pathlib import Path

# Paths
source_path = r'C:\Users\hp\Documents\MscCSULB\SEM2\CECS-551-AdvanceArtificialIntelligence\Research_Project\Sign-Language-Digits-Dataset\Dataset'  # Change to your dataset path
destination_path = 'new_dataset'  # Change to where you want the new dataset

# Create the destination directory if it doesn't exist
Path(destination_path).mkdir(parents=True, exist_ok=True)

# Iterate over each subfolder in the dataset
for folder in os.listdir(source_path):
    folder_path = os.path.join(source_path, folder)
    
    # Check if it's a directory
    if os.path.isdir(folder_path):
        # Create corresponding directory in the new dataset folder
        new_folder_path = os.path.join(destination_path, folder)
        Path(new_folder_path).mkdir(parents=True, exist_ok=True)
        
        # Get the first 30 images
        images = os.listdir(folder_path)[:30]
        
        # Copy each image to the new directory
        for img in images:
            src_img_path = os.path.join(folder_path, img)
            dst_img_path = os.path.join(new_folder_path, img)
            shutil.copy2(src_img_path, dst_img_path)

print("Dataset creation complete.")
