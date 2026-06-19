import torch

# Task 2: Generate input data - create a non-singular 2x2 tensor
input_data = torch.tensor([[4., 7.], [2., 6.]])

# Task 3: Call the API
result = torch.linalg.inv(input_data)