import torch

# Task 2: Generate input data
matrix = torch.tensor([[4, 7], [2, 6]], dtype=torch.float32)

# Task 3: Call the API torch.linalg.det
result = torch.linalg.det(matrix)
print(result)