import torch

# Prepare valid input data
f = 'path/to/model.pth'  # Replace with actual file path
map_location = 'cpu'

# Call the API
result = torch.load(f, map_location=map_location)