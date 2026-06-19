import torch
from torch.utils.data import DataLoader, TensorDataset

# Create a dummy dataset
data = torch.randn(10, 3)
dataset = TensorDataset(data)

# Initialize DataLoader
dataloader = DataLoader(dataset, batch_size=2, shuffle=False)