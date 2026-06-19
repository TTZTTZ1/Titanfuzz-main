import torch

# Task 2: Generate input data
tensor = torch.randn(10, 5)  # A tensor of shape (10, 5)

# Task 3: Call the API
split_tensors = tensor.split(split_size=2, dim=0)