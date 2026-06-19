import torch

# Step 2: Generate input data
data = torch.randn(4, 5)

# Step 3: Call the API
result = torch.transpose(data, 0, 1)