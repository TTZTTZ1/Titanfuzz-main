import torch

# Task 2: Generate input data
input_tensor = torch.randn(3, 4)

# Task 3: Call the API torch.Tensor.float
result = input_tensor.float(memory_format=torch.preserve_format)