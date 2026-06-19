import torch

# Task 2: Generate input data - a 2x2 matrix
input_data = torch.tensor([[4.0, 7.0], [2.0, 6.0]])

# Task 3: Call the API torch.linalg.inv
result = torch.linalg.inv(input_data)
print(result)