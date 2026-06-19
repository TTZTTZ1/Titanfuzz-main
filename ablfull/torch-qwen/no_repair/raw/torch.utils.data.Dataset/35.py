import torch

# Task 2: Generate input data
data = torch.randn(4, 3, 224, 224)  # Example tensor of shape (batch_size, channels, height, width)

# Task 3: Call the API
dataset = torch.utils.data.Dataset(data)