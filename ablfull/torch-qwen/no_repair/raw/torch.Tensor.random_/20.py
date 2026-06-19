import torch

# Prepare valid input data
dtype = torch.float
from_val = 0
to_val = 5

# Create a tensor with random values
result = torch.Tensor().random_(from_=from_val, to=to_val, dtype=dtype)
print(result)