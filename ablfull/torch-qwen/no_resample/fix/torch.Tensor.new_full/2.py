import torch
size = (2, 3)
fill_value = 5
dtype = torch.int
device = torch.device('cpu')
requires_grad = False
layout = torch.strided
pin_memory = False
result = torch.tensor([0], dtype=torch.float).new_full(size, fill_value, dtype=dtype, device=device, requires_grad=requires_grad, layout=layout, pin_memory=pin_memory)