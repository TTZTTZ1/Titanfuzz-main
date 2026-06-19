import torch

# Task 2: Generate input data
input_tensor = torch.randn(2, 3, 5)
mat2_tensor = torch.randn(2, 5, 4)

# Task 3: Call the API torch.bmm
result = torch.bmm(input_tensor, mat2_tensor)
print(result)