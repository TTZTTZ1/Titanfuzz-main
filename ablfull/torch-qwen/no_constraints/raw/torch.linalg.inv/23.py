import torch

# Task 2: Generate input data
input_data = torch.tensor([[4., 7.], [2., 6.]], dtype=torch.float32)

# Task 3: Call the API
result = torch.linalg.inv(input_data)