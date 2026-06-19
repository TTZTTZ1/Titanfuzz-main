import torch

size = 5
fill_value = 3.0
dtype = torch.float
device = torch.device('cpu')
requires_grad = False
layout = torch.strided
pin_memory = False

tensor = torch.Tensor.new_full((size,), fill_value, dtype=dtype, device=device, requires_grad=requires_grad, layout=layout, pin_memory=pin_memory)