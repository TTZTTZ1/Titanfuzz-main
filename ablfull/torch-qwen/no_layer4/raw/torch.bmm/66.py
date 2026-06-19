import torch

# Prepare valid input data
input_tensor = torch.randn(5, 10, 3)
mat2_tensor = torch.randn(5, 3, 8)

# Call the target API
result = torch.bmm(input_tensor, mat2_tensor)