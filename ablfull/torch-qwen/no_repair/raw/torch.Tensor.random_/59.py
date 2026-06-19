import torch

# Prepare input data
dtype = torch.float32
from_val = 0
to_val = 5

# Create a random tensor
tensor_random = torch.Tensor.random_(dtype=dtype, from_=from_val, to=to_val)
print(tensor_random)