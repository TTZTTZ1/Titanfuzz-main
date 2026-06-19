import torch

# Prepare input data
input_tensor = torch.randn(5, 2, 3)
mat2_tensor = torch.randn(5, 3, 4)

# Call the API
result = torch.bmm(input_tensor, mat2_tensor)