import torch
batch_size = 2
matrices1 = torch.randn(batch_size, 3, 4)
matrices2 = torch.randn(batch_size, 4, 5)
result = torch.bmm(matrices1, matrices2)