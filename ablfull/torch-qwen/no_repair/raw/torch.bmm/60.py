import torch

# Prepare valid input data
input_tensor = torch.randn(2, 3, 5)
mat2_tensor = torch.randn(2, 5, 4)

# Call the target API
result = torch.bmm(input_tensor, mat2_tensor)