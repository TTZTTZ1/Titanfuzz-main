import torch
from torch.utils.data import DataLoader

# Prepare valid input data
dataset = torch.randn(100, 3, 256, 256)
batch_size = 4
shuffle = True

# Call the API
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=shuffle)