import torch
from torch.utils.data import DataLoader, TensorDataset

# Prepare valid input data
data = torch.randn(10, 3, 224, 224)
dataset = TensorDataset(data)

# Call the API
dataloader = DataLoader(dataset, batch_size=2, shuffle=True)