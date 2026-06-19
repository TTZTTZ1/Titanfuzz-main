import torch

# Prepare valid input data
dtype = torch.int
from_val = 0
to_val = 5

# Create a tensor with random values
result = torch.tensor(0, dtype=dtype)
result.random_(from_val, to_val)

print(result)