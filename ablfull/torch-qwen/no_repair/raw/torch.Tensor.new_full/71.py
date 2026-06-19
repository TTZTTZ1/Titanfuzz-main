import torch

# Generate input data
size = (3, 4)
fill_value = 5
dtype = None
device = 'cpu'
requires_grad = False
layout = torch.strided
pin_memory = True

# Ensure the constraint is satisfied
if pin_memory and device != 'cpu':
    device = 'cpu'

# Call the API
tensor = torch.Tensor.new_full(size, fill_value, dtype=dtype, device=device, requires_grad=requires_grad, layout=layout, pin_memory=pin_memory)