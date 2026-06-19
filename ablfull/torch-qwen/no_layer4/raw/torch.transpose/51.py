import torch

# Generate a random tensor
input_tensor = torch.randn(4, 4)

# Define dimensions for transpose
dim0 = 0
dim1 = 1

# Call the API
result = torch.transpose(input_tensor, dim0, dim1)