import torch

# Task 2: Generate input data
input_tensor = torch.randn(4, 4)

# Task 3: Call the API
stride_result = input_tensor.stride()
print(stride_result)