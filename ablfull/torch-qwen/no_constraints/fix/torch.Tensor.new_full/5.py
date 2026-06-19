import torch
shape = (3,)
fill_value = 5.0
dtype = torch.float32
layout = torch.strided
device = 'cpu'
requires_grad = False
output_tensor = torch.tensor([0], dtype=dtype, device=device).new_full(shape, fill_value, dtype=dtype, layout=layout, device=device, requires_grad=requires_grad)