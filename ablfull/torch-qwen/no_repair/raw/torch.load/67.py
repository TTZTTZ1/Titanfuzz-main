import torch

# Prepare valid input data
f = 'path_to_your_file.pth'
map_location = 'cpu'

# Call the API
data = torch.load(f, map_location=map_location)