
import torch
dataset = torch.utils.data.TensorDataset(torch.randn(10, 3))
batch_size = 2
shuffle = False
sampler = None
num_workers = 0
pin_memory = False
drop_last = False
dataloader = torch.utils.data.DataLoader(dataset, batch_size=batch_size, shuffle=shuffle, sampler=sampler, num_workers=num_workers, pin_memory=pin_memory, drop_last=drop_last)
