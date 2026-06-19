import torch

# Generate valid input data
matrix = torch.tensor([[4., 7.], [2., 6.]])

# Call the API
result = torch.slogdet(matrix)

print(result)