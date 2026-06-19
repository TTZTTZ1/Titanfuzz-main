import torch

# Generate valid input data
input_tensor = torch.randn(2, 3, 5)
mat2_tensor = torch.randn(2, 5, 4)

# Call the API
result = torch.bmm(input_tensor, mat2_tensor)