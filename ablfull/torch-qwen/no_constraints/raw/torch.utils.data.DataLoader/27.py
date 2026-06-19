import torch
from torch.utils.data import DataLoader

# Task 2: Generate input data
dataset = torch.randn(100, 10)

# Task 3: Call the API
dataloader = DataLoader(dataset, batch_size=5)