import torch

# Task 2: Generate input data
size = (3, 4)
fill_value = 5.0
dtype = torch.float32
layout = torch.strided
device = 'cpu'
requires_grad = False

# Task 3: Call the API
result = torch.Tensor.new_full(size, fill_value, dtype=dtype, layout=layout, device=device, requires_grad=requires_grad)
print(result)