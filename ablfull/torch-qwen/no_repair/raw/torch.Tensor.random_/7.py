import torch

# Generate valid input data
dtype = torch.float
from_val = 0
to_val = 10

# Create a random tensor
tensor = torch.Tensor().random_(from_val, to_val, dtype=dtype)
print(tensor)