import torch

# Generate valid input data
f = 'path/to/model.pth'  # Replace with actual file path or PathLike object
map_location = 'cpu'
pickle_module = None
weights_only = True
mmap = None
pickle_load_args = {}

# Call the API
model = torch.load(f, map_location=map_location, pickle_module=pickle_module, weights_only=weights_only, mmap=mmap, **pickle_load_args)