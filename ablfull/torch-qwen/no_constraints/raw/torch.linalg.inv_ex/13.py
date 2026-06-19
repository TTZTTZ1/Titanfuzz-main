import torch

# Task 2: Generate input data
input_tensor = torch.tensor([[4., 7.], [2., 6.]], dtype=torch.float32)

# Task 3: Call the API
result = torch.linalg.inv_ex(input_tensor)