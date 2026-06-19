import torch

# Task 2: Generate input data
input_tensor = torch.randn(2, 3, 4)
dims = (2, 0, 1)

# Task 3: Call the API
result = input_tensor.permute(dims)

print(result.shape)  # Output should be torch.Size([4, 2, 3])