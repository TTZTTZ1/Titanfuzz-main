import torch

# Create random tensors
input_tensor = torch.randn(5, 3)
mat2_tensor = torch.randn(3, 4)

# Perform matrix multiplication
result_tensor = torch.mm(input_tensor, mat2_tensor)

print(result_tensor)