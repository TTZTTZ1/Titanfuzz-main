import torch

# Task 2: Generate input data - a square matrix of size 2x2
input_matrix = torch.tensor([[4.0, 7.0], [2.0, 6.0]], dtype=torch.float32)

# Task 3: Call the API torch.linalg.det
result = torch.linalg.det(input_matrix)
print(result)