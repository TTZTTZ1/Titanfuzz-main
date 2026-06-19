import torch

# Generate a 3x3 invertible matrix as input data
input_matrix = torch.tensor([[4.0, 7.0], [2.0, 6.0]])

# Call the torch.linalg.inv_ex API
result = torch.linalg.inv_ex(input_matrix)

print(result)