import torch

# Generate a non-sparse tensor
input_tensor = torch.randn(4, 5)

# Define dimensions to transpose
dim0 = 0
dim1 = 1

# Call torch.transpose
result = torch.transpose(input_tensor, dim0, dim1)