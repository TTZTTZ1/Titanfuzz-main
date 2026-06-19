import torch

# Step 2: Generate input data
tensor = torch.randn(2, 3, 4)
dims = (2, 0, 1)

# Step 3: Call the API
permuted_tensor = tensor.permute(dims)