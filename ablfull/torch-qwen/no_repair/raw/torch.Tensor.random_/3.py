import torch

# Prepare valid input data
dtype = torch.float
from_val = 0
to_val = 5

# Create a random tensor
tensor = torch.tensor([1.0], dtype=dtype)
tensor.random_(from_val, to_val)

print(tensor)