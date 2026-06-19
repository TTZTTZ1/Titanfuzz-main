import torch

# Prepare valid input data
dtype = 'int'
from_val = 0
to_val = 5

# Create a random tensor using the provided parameters
tensor = torch.tensor(0, dtype=torch.int)
tensor.random_(from_=from_val, to=to_val)

print(tensor)