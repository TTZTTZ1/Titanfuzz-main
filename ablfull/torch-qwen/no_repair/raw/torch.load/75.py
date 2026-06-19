import torch

# Prepare valid input data
f = 'example.pt'  # Path to your file
map_location = torch.device('cpu')

# Call the API
result = torch.load(f, map_location=map_location)