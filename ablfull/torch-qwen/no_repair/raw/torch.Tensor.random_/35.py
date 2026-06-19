import torch

# Generate valid input data
dtype = torch.float
from_val = 0
to_val = 1

# Call the API
result = torch.Tensor().random_(from_=from_val, to=to_val, dtype=dtype)
print(result)