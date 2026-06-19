import torch

# Task 2: Generate input data
size = (2, 3)
fill_value = 5
dtype = torch.int
device = torch.device('cpu')
requires_grad = False

# Task 3: Call the API
result = torch.Tensor.new_full(size, fill_value, dtype=dtype, device=device, requires_grad=requires_grad)
print(result)