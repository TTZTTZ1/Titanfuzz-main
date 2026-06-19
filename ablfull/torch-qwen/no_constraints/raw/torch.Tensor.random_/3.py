import torch

# Generate input data
size = (3, 4)
dtype = torch.float32
layout = torch.strided
device = 'cpu'
requires_grad = False

# Call the API
result = torch.Tensor().random_(size=size, dtype=dtype, layout=layout, device=device, requires_grad=requires_grad)
print(result)