import torch
dataset = torch.utils.data.TensorDataset(torch.randn(10, 3))
dataloader = torch.utils.data.DataLoader(dataset, batch_size=2, shuffle=False)