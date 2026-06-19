import torch
from torch.utils.data import DataLoader, TensorDataset

# Prepare valid input data
data = torch.randn(100, 3, 256, 256)
dataset = TensorDataset(data)

# Call the API
dataloader = DataLoader(dataset, batch_size=4, shuffle=True)