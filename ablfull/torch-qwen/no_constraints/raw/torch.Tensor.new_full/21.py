import torch

# Prepare valid input data
shape = (3,)
fill_value = 5.0
dtype = torch.float32
layout = torch.strided
device = 'cpu'
requires_grad = False

# Call the API
result = torch.Tensor.new_full(shape, fill_value, dtype=dtype, layout=layout, device=device, requires_grad=requires_grad)