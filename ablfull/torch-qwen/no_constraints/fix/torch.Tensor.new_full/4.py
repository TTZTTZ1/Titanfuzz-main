import torch
size = (3,)
fill_value = 5.0
dtype = torch.float32
layout = torch.strided
device = 'cpu'
requires_grad = False
input_tensor = torch.tensor([], dtype=torch.float32)
output = input_tensor.new_full(size, fill_value, dtype=dtype, layout=layout, device=device, requires_grad=requires_grad)
print(output)