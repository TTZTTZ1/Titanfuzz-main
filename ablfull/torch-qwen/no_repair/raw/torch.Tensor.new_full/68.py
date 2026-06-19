import torch

# Generate input data
size = (2, 3)
fill_value = 5.0
dtype = torch.float32
requires_grad = True

# Call the API
result = torch.Tensor.new_full(size, fill_value, dtype=dtype, requires_grad=requires_grad)