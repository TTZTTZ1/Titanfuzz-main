import torch
shape = (2, 3)
fill_value = 5.0
dtype = torch.float32
layout = torch.strided
device = 'cpu'
requires_grad = False
tensor = torch.tensor([], dtype=torch.float32)
result = tensor.new_full(shape, fill_value, dtype=dtype, layout=layout, device=device, requires_grad=requires_grad)
print(result)