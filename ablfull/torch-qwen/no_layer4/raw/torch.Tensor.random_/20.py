import torch

# Prepare valid input data
dtype = torch.float
from_val = 0
to_val = 5

# Create a tensor of random values
tensor = torch.tensor(0, dtype=dtype)
tensor.random_(from_val, to_val)

print(tensor)