import torch

# Prepare input data
size = (2, 3)
fill_value = 5
dtype = torch.int
requires_grad = False

# Call the API
result = torch.Tensor.new_full(size, fill_value, dtype=dtype, requires_grad=requires_grad)

print(result)