import torch

# Prepare input data
size = (2, 3)
fill_value = 5.0
dtype = torch.float32

# Call the API
output = torch.Tensor.new_full(size=size, fill_value=fill_value, dtype=dtype)

print(output)