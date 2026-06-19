import torch

# Prepare valid input data
dtype = 'float'
from_val = 0
to_val = 10

# Call the API
result = torch.Tensor.random_(dtype=dtype, from_=from_val, to=to_val)
print(result)