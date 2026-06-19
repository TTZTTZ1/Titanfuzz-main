import torch

# Generate input data
input_data = torch.randn(2, 3, 4)
mat2 = torch.randn(2, 4, 5)

# Call the API
result = torch.bmm(input_data, mat2)