import torch

# Generate input data
input_data = torch.randn(2, 3, 5)
mat2_data = torch.randn(2, 5, 4)

# Call the API
result = torch.bmm(input_data, mat2_data)