import torch

# Prepare valid input data
dtype = 'int'
from_val = 0
to_val = 5

# Create a tensor of random integers between 0 and 5
tensor = torch.tensor(0, dtype=torch.int)
tensor.random_(from_val, to_val)

print(tensor)