import torch
from torch.utils.data import DataLoader

# Prepare valid input data
dataset = torch.randn(100, 3, 224, 224)
batch_size = 16
shuffle = True

# Call the API
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=shuffle)