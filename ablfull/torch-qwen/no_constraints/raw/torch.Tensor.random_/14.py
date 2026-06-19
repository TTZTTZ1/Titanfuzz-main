import torch

# Generate input data
shape = (2, 3)
dtype = torch.float32
layout = torch.strided
device = 'cpu'
requires_grad = False

# Call the API
result = torch.Tensor().random_(size=shape, dtype=dtype, layout=layout, device=device, requires_grad=requires_grad)