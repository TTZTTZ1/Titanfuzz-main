import torch

# Task 2: Generate input data
size = (2, 3)
fill_value = 5
dtype = torch.int
device = None
requires_grad = False
layout = torch.strided
pin_memory = True

# Task 3: Call the API
tensor = torch.tensor.new_full(size, fill_value, dtype=dtype, device=device,
                               requires_grad=requires_grad, layout=layout,
                               pin_memory=pin_memory)