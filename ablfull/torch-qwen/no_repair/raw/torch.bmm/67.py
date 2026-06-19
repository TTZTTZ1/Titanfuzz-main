import torch

# Task 2: Generate input data
input_tensor = torch.randn(3, 5, 8)
mat2_tensor = torch.randn(3, 8, 6)

# Task 3: Call the API
result = torch.bmm(input_tensor, mat2_tensor)
print(result)