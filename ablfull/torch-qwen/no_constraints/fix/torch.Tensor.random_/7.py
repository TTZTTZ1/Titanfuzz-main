import torch
shape = (3, 4)
dtype = torch.float32
device = 'cpu'
requires_grad = False
result = torch.empty(shape, dtype=dtype, device=device, requires_grad=requires_grad).random_()
print(result)