import torch

# Task 2: Generate input data
data = torch.randn(2, 3, 4)
dims = (1, 0, 2)

# Task 3: Call the API torch.Tensor.permute
result = data.permute(dims)