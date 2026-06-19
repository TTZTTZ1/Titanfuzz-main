import torch

# Task 2: Generate input data
input_tensor = torch.randn(3)

# Task 3: Call the API torch.Tensor.stride
stride_result = input_tensor.stride(None)
print(stride_result)