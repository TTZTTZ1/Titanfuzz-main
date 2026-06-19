import torch

# Step 2: Generate input data
data = torch.randn(2, 3, 4)

# Step 3: Call the API
result = data.permute(1, 0, 2)