import torch
shape = (3, 4)
dtype = torch.float32
device = 'cpu'
requires_grad = False
tensor = torch.empty(shape, dtype=dtype, device=device, requires_grad=requires_grad)
tensor.random_()