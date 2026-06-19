import torch

# Task 2: Generate input data
tensor = torch.randn(3, 4)

# Task 3: Call the API torch.Tensor.stride
stride_result = tensor.stride()
print(stride_result)