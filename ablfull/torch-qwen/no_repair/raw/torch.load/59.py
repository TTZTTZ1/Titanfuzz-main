import torch

# Prepare valid input data
f = 'path_to_your_file.pth'
map_location = None
pickle_module = None
weights_only = True
mmap = None
pickle_load_args = {}

# Call the API
result = torch.load(f, map_location=map_location, pickle_module=pickle_module, weights_only=weights_only, mmap=mmap, **pickle_load_args)