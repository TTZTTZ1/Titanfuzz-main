import torch
dataset = torch.utils.data.TensorDataset(torch.randn(10, 3))
dataloader = torch.utils.data.DataLoader(dataset=dataset, batch_size=2, shuffle=False, num_workers=0, prefetch_factor=None)