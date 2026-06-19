import torch

# Prepare valid input data
input_tensor = torch.randn(10, 5, 8)
mat2_tensor = torch.randn(10, 8, 3)

# Call the API
result = torch.bmm(input_tensor, mat2_tensor)
print(result)