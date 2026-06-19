import torch

# Create a dense tensor
input_tensor = torch.randn(4, 5)

# Define dimensions to transpose
dim0 = 0
dim1 = 1

# Call torch.transpose
transposed_tensor = torch.transpose(input_tensor, dim0, dim1)