import torch

# Generate valid input data
dtype = torch.float
from_val = 0
to_val = 5

# Create a random tensor with specified parameters
tensor = torch.Tensor().random_(from=from_val, to=to_val, dtype=dtype)