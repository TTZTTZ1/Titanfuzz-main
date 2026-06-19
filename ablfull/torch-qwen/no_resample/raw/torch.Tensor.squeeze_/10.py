import torch

# Task 2: Generate input data
input_tensor = torch.randn(1, 1, 3, 4)

# Task 3: Call the API
result = input_tensor.squeeze_(dim=(0, 1))