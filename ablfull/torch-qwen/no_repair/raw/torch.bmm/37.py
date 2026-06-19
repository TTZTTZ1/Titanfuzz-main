import torch

# Task 2: Generate input data
input_tensor = torch.randn(2, 3, 4)
mat2_tensor = torch.randn(2, 4, 5)

# Task 3: Call the API torch.bmm
result = torch.bmm(input_tensor, mat2_tensor)