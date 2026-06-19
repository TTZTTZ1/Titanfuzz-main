import torch

# Create two random 2D tensors
input_tensor = torch.randn(3, 4)
mat2_tensor = torch.randn(4, 5)

# Perform matrix multiplication
result_tensor = torch.mm(input_tensor, mat2_tensor)

print(result_tensor)