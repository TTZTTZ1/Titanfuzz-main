import torch
size = (3, 4)
dtype = torch.float32
layout = torch.strided
device = 'cpu'
requires_grad = False
result = torch.empty(size, dtype=dtype, layout=layout, device=device, requires_grad=requires_grad).random_()