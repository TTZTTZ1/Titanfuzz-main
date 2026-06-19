import torch

# Prepare valid input data
file_path = 'path_to_your_file.pth'
map_location = None

# Call the API
data = torch.load(file_path, map_location=map_location)