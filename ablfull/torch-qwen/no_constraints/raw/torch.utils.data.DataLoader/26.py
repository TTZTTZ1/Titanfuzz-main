import torch
from torch.utils.data import DataLoader

# Prepare valid input data
dataset = torch.rand(10, 5)  # Example dataset of shape (10, 5)
batch_size = 2

# Call the API
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)