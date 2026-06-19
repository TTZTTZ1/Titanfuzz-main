
import torch
dataset = torch.utils.data.TensorDataset(torch.randn(10))
batch_size = 2
shuffle = True
num_workers = 0
dataloader = torch.utils.data.DataLoader(dataset=dataset, batch_size=batch_size, shuffle=shuffle, num_workers=num_workers)
