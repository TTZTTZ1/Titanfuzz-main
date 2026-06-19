import torch

# Prepare valid input data
dtype = torch.float
from_value = 0
to_value = 1

# Call the API
result = torch.Tensor().random_(from_=from_value, to=to_value, dtype=dtype)
print(result)