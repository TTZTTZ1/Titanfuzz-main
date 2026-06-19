import torch

# Prepare valid input data
dtype = torch.float
from_val = 0
to_val = 10

# Call the API
result = torch.Tensor().random_(from_=from_val, to=to_val, dtype=dtype)