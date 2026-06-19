
import torch
f = 'example.pth'
map_location = None
pickle_module = None
weights_only = True
mmap = None
pickle_load_args = {}
data = torch.load(f, map_location=map_location, pickle_module=pickle_module, weights_only=weights_only, mmap=mmap, **pickle_load_args)
