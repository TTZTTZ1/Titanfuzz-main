import torch
batch1 = torch.randn(10, 3, 5)
batch2 = torch.randn(10, 5, 4)
result = torch.bmm(batch1, batch2)