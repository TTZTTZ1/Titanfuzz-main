import torch
from torch.utils.data import DataLoader, TensorDataset

# Prepare valid input data
data = torch.randn(10, 5)
dataset = TensorDataset(data)
batch_size = 2
shuffle = True

# Call the API
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=shuffle)