import torch

# Prepare valid input data
f = 'path_to_your_file.pth'  # Replace with the actual file path
map_location = torch.device('cpu')  # Replace with the desired device

# Call the API
result = torch.load(f, map_location=map_location)