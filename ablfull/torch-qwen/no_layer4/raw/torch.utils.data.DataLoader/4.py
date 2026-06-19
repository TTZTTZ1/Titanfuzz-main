import torch
from torch.utils.data import DataLoader, TensorDataset

# Create a dummy dataset
data = torch.randn(10, 3)
dataset = TensorDataset(data)

# Prepare valid input parameters
batch_size = 2
shuffle = False
num_workers = 0

# Call the API
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=shuffle, num_workers=num_workers)