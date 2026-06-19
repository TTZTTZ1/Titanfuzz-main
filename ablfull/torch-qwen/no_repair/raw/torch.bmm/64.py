import torch

# Prepare input data
input_tensor = torch.randn(5, 3, 6)
mat2_tensor = torch.randn(5, 6, 7)

# Call the API
output = torch.bmm(input_tensor, mat2_tensor)