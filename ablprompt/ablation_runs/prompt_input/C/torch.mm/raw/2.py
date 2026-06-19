import torch

# Create two random 2D tensors
input_tensor = torch.randn(5, 3)
mat2_tensor = torch.randn(3, 4)

# Perform matrix multiplication using torch.mm
result_tensor = torch.mm(input_tensor, mat2_tensor)

print(result_tensor)