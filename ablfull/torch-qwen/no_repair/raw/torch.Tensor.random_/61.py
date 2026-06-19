import torch

# Prepare valid input data
dtype = torch.float
from_ = 0
to = 10

# Create the tensor
result = torch.tensor(0., dtype=dtype)
result.random_(from_, to)

print(result)