import torch
from torch.utils.data import DataLoader
dataset = torch.utils.data.TensorDataset(torch.randn(10, 3), torch.randint(0, 2, (10,)))
batch_size = 4
shuffle = True
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=shuffle)