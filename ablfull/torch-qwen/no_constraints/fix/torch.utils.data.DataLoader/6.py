import torch
from torch.utils.data import DataLoader, TensorDataset
data = torch.randn(10, 5)
dataset = TensorDataset(data)
dataloader = DataLoader(dataset, batch_size=2, shuffle=True)