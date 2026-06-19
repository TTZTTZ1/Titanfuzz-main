import torch

# Task 2: Generate input data
input_tensor = torch.tensor([[4., 7.], [2., 6.]])

# Task 3: Call the API
result = torch.linalg.det(input_tensor)
print(result)