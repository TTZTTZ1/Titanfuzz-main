import torch

# Task 2: Generate input data
data = torch.randn(4, 4)

# Task 3: Call the API
stride_result = data.stride()

print(stride_result)