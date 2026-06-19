import torch

# Prepare valid input data
shape = (3, 4)
dtype = torch.float32
layout = torch.strided
device = 'cpu'
requires_grad = False

# Call the API
result = torch.Tensor(shape, dtype=dtype, layout=layout, device=device, requires_grad=requires_grad).random_()