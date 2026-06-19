import torch

# Prepare valid input data
dtype = 'int'
from_val = -5
to_val = 5

# Create a random tensor within the specified range
tensor = torch.tensor(0, dtype=torch.int)
tensor.random_(from_val, to_val)

print(tensor)