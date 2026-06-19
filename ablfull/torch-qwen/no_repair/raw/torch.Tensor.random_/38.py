import torch

# Prepare valid input data
dtype = torch.float
from_val = 0
to_val = 5

# Create input tensor
input_tensor = torch.tensor(from_val, dtype=dtype)

# Call the API
result = input_tensor.random_(from_=from_val, to=to_val)