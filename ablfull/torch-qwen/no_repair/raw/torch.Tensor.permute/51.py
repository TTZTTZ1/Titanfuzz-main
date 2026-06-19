import torch

# Task 2: Prepare valid input data
tensor = torch.randn(2, 3, 4)

# Task 3: Call the API
permuted_tensor = tensor.permute((2, 0, 1))