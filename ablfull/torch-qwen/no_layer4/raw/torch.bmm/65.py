import torch

# Task 2: Generate input data
input_data = torch.randn(2, 3, 4)
mat2_data = torch.randn(2, 4, 5)

# Call the API torch.bmm
result = torch.bmm(input_data, mat2_data)