
import torch
from torch.utils.data import DataLoader, TensorDataset
dataset = TensorDataset(torch.randn(10, 3), torch.randint(0, 2, (10,)))
batch_size = 2
shuffle = False
num_workers = 0
pin_memory = False
drop_last = False
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=shuffle, num_workers=num_workers, pin_memory=pin_memory, drop_last=drop_last)
