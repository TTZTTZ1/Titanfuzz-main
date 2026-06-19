import torch

# Generate valid input data
input_tensor = torch.randn(3, 2, 4)
mat2_tensor = torch.randn(3, 4, 5)

# Call the API
result = torch.bmm(input_tensor, mat2_tensor)