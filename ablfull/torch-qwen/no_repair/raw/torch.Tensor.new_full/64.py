import torch

# Task 2: Generate input data
size = (3, 4)
fill_value = 7.0
dtype = torch.float
layout = torch.strided

# Task 3: Call the API
tensor = torch.Tensor.new_full(size, fill_value, dtype=dtype, layout=layout)