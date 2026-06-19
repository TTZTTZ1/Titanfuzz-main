import torch

# Task 2: Generate input data
input_tensor = torch.randn(3, 4, 5)

# Task 3: Call the API torch.Tensor.permute
permuted_tensor = input_tensor.permute(2, 0, 1)