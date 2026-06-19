import torch
from torch.utils.data import DataLoader

# Prepare valid input data
dataset = torch.randn(100, 3, 224, 224)  # Example dataset of images
batch_size = 8

# Call the API
dataloader = DataLoader(dataset, batch_size=batch_size)