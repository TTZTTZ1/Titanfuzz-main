import torch

# Task 2: Generate input data - create a square tensor of size 3x3 with random values
input_data = torch.randn(3, 3)

# Task 3: Call the API torch.linalg.det
result = torch.linalg.det(input_data)