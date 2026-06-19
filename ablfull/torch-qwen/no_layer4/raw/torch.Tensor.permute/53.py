import torch

# Step 2: Generate input data
tensor = torch.randn(3, 4)
dims = (1, 0)

# Step 3: Call the API
result = tensor.permute(dims)
print(result)