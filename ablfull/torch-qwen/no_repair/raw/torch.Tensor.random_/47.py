import torch

# Prepare valid input data
dtype = torch.float
from_val = 0
to_val = 1

# Call the API
result = torch.tensor([from_val], dtype=dtype).random_(from_val, to_val)
print(result)