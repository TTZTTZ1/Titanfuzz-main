import torch

# Prepare valid input data
dtype = torch.float
from_value = 0
to_value = None

# Call the API
result = torch.tensor([0.5], dtype=dtype)
result.random_(from_=from_value, to=to_value)