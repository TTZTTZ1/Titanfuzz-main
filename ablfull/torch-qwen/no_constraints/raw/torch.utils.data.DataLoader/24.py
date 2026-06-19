import torch
from torch.utils.data import DataLoader, TensorDataset

# Prepare valid input data
data = torch.randn(100, 10)
dataset = TensorDataset(data)

# Call the API
dataloader = DataLoader(dataset, batch_size=5, shuffle=True)