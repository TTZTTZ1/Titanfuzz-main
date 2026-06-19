import torch

# Step 2: Generate input data
tensor = torch.randn(2, 3)
dims = (1, 0)

# Step 3: Call the API
permuted_tensor = tensor.permute(dims)