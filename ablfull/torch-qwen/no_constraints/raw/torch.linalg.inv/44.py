import torch

# Task 2: Generate input data
input_matrix = torch.tensor([[4.0, 7.0], [2.0, 6.0]])

# Task 3: Call the API torch.linalg.inv
inverse_matrix = torch.linalg.inv(input_matrix)

print(inverse_matrix)