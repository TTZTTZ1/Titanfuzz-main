import torch
from torch.utils.data import DataLoader, TensorDataset
data = torch.randn(100, 3)
dataset = TensorDataset(data)
dataloader = DataLoader(dataset, batch_size=5, shuffle=True)