import torch
from torch.utils.data import DataLoader, TensorDataset
data = torch.randn(10, 3, 224, 224)
dataset = TensorDataset(data)
dataloader = DataLoader(dataset, batch_size=5, shuffle=True)