import torch

# Prepare valid input data
dtype = 'float'
from_val = 0
to_val = 1

# Create a random tensor within the specified range and dtype
tensor = torch.empty(1).random_(from_val, to_val, dtype=torch.float)