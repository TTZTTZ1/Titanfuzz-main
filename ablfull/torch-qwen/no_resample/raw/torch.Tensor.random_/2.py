import torch

# Generate valid input data
dtype = 'float'
from_val = 0
to_val = 1

# Create a random tensor
tensor = torch.empty(1, dtype=torch.float)
tensor.random_(from_val, to_val)

print(tensor)