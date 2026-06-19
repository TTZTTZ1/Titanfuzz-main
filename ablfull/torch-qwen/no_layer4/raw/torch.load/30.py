import torch

# Prepare valid input data
f = 'path_to_your_file.pth'  # Replace with actual file path
map_location = None  # or specify a device like torch.device('cpu') or torch.device('cuda')

# Call the API
result = torch.load(f, map_location=map_location)