import torch

# Step 2: Generate input data
data = [{'input': torch.randn(3), 'label': 0} for _ in range(4)]

# Step 3: Call the API
dataset = torch.utils.data.Dataset()