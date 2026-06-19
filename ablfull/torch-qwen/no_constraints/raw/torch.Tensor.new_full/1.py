import torch

# Task 2: Generate input data
shape = (2, 3)
fill_value = 5.0
dtype = torch.float32

# Task 3: Call the API
result = torch.Tensor.new_full(shape, fill_value, dtype=dtype)

print(result)