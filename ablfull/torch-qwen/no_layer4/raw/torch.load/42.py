import torch

# Prepare valid input data
f = 'path_to_your_file.pth'  # Replace with the actual file path
map_location = None  # You can also use a specific device like 'cpu' or 'cuda'

# Call the API
result = torch.load(f, map_location=map_location)