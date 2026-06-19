import torch

# Prepare valid input data
file_path = 'path/to/your/file.pth'
map_location = 'cpu'

# Call the API
data = torch.load(file_path, map_location=map_location)