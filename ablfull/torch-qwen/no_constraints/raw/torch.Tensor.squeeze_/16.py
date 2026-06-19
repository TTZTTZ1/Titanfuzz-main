import torch

# Task 2: Generate input data
input_tensor = torch.randn(1, 3, 1, 4)

# Task 3: Call the API
result = input_tensor.squeeze_()