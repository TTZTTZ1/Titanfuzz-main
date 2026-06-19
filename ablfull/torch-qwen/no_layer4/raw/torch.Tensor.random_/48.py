import torch

# Prepare valid input data
dtype = torch.float
from_val = 0
to_val = 1

# Create a random tensor
tensor = torch.zeros(5)
tensor.random_(from_val, to_val)

print(tensor)