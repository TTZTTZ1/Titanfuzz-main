import torch

# Step 2: Prepare valid input data
data = torch.randn(2, 3, 4)
dims = (2, 0, 1)

# Step 3: Call the API
result = data.permute(*dims)