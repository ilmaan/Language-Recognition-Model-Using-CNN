import os
from pathlib import Path

# Path to the dataset directory
dataset_path = Path(r'new_dataset')

# Iterate over each subdirectory in the dataset directory
for folder in os.listdir(dataset_path):
    folder_path = dataset_path / folder
    
    # Check if it is a directory
    if folder_path.is_dir():
        # List all image files in the directory
        files = sorted(folder_path.glob('*.jpg'), key=os.path.getmtime)
        
        # Rename each file in sequential order
        for i, file in enumerate(files):
            new_file_name = f"{i}.jpg"
            new_file_path = folder_path / new_file_name
            os.rename(file, new_file_path)

print("Files have been renamed successfully.")
