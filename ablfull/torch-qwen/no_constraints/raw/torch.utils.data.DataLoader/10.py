import torch
from torch.utils.data import DataLoader

# Prepare valid input data
dataset = torch.utils.data.TensorDataset(torch.randn(10, 5))
batch_size = 2
shuffle = True

# Call the API
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=shuffle)