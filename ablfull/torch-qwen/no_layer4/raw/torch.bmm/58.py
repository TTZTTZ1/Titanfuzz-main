import torch

# Prepare valid input data
input_tensor = torch.randn(10, 5, 3)
mat2_tensor = torch.randn(10, 3, 6)

# Call the API
output_tensor = torch.bmm(input_tensor, mat2_tensor)