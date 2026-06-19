import torch

# Task 2: Generate input data
input_data = torch.tensor([[4., 7.], [2., 6.]])  # Ensure it's invertible

# Task 3: Call the API
result = torch.linalg.inv_ex(input_data)

print(result)