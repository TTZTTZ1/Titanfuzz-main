import torch
from torch.utils.data import DataLoader

# Create a dummy dataset
dataset = torch.randn(10, 3)

# Initialize DataLoader with valid parameters
dataloader = DataLoader(dataset, batch_size=2, shuffle=False)