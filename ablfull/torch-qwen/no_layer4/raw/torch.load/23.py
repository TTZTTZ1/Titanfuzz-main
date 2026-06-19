import torch

# Generate input data
f = 'path_to_your_file.pth'  # Replace with actual file path
map_location = 'cpu'
weights_only = True

# Call the API
result = torch.load(f, map_location=map_location, weights_only=weights_only)