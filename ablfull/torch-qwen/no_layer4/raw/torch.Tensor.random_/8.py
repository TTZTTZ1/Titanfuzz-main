import torch

# Prepare valid input data
dtype = torch.float
from_val = 0
to_val = 10

# Call the API
result = torch.tensor([from_val, to_val], dtype=dtype)
print(result)