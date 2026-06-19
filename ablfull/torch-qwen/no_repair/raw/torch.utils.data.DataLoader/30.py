import torch
from torch.utils.data import DataLoader, TensorDataset

# Prepare valid input data
dataset = TensorDataset(torch.randn(10, 3), torch.randint(0, 2, (10,)))
batch_size = 2
shuffle = True
num_workers = 0

# Create DataLoader instance
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=shuffle, num_workers=num_workers)