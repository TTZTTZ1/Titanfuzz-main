import torch

# Task 2: Generate input data
shape = (3, 4)
dtype = torch.float32

# Task 3: Call the API
tensor = torch.Tensor(shape).random_(min=0, max=10, dtype=dtype)
print(tensor)