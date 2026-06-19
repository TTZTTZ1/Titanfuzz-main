import torch

# Task 2: Generate input data
input_tensor = torch.tensor([[4., 7.], [2., 6.]])  # Valid input for torch.linalg.det

# Task 3: Call the API
result = torch.linalg.det(input_tensor)

print(result)