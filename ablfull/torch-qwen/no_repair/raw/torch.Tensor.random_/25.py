import torch

# Prepare valid input data
dtype = 'int'
from_val = 0
to_val = 5

# Create a random tensor
tensor = torch.Tensor().random_(from_=from_val, to=to_val)
print(tensor)