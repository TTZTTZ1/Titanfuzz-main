import torch

# Prepare valid input data
f = 'path_to_your_file.pt'  # Replace with actual file path
map_location = 'cpu'

# Call the API
result = torch.load(f, map_location=map_location)