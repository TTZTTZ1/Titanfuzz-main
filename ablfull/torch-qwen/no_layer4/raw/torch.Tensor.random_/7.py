import torch

# Generate valid input data
dtype = torch.float
from_val = 0
to_val = 5

# Create a tensor of random numbers
tensor = torch.tensor([0], dtype=dtype)
tensor.random_(from_val, to_val)

print(tensor)