import torch

# Generate input data
size = (3, 4)
fill_value = 7.5
dtype = torch.float
device = None
requires_grad = False
layout = torch.strided
pin_memory = False

# Call the API
result = torch.Tensor.new_full(size, fill_value, dtype=dtype, device=device, requires_grad=requires_grad, layout=layout, pin_memory=pin_memory)

print(result)