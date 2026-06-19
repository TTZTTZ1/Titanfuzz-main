import torch
from torch.utils.data import DataLoader

# Prepare valid input data
dataset = torch.randn(100, 10)
batch_size = 5
shuffle = True

# Call the API
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=shuffle)