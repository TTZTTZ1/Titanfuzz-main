import torch

# Prepare valid input data
dtype = torch.float
from_val = 0
to_val = 1

# Call the API
tensor = torch.tensor(0.5, dtype=dtype)
tensor.random_(from_val, to_val)