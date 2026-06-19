import torch
from torch.utils.data import DataLoader

# Create a dummy dataset
dataset = torch.randn(10, 5)

# Prepare valid input data
batch_size = 2
shuffle = True

# Call the API
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=shuffle)