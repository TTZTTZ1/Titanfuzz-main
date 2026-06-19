import torch
shape = (2, 3)
dtype = torch.float32
layout = torch.strided
device = 'cpu'
requires_grad = False
tensor = torch.empty(shape, dtype=dtype, layout=layout, device=device, requires_grad=requires_grad)
tensor.random_()