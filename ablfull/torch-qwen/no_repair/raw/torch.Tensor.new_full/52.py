import torch

size = (2, 3)
fill_value = 5.0
dtype = torch.float
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
requires_grad = False

tensor = torch.tensor.new_full(size, fill_value, dtype=dtype, device=device, requires_grad=requires_grad)
print(tensor)