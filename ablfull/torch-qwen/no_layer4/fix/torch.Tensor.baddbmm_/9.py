import torch
self_tensor = torch.randn(4, 5, 6)
batch1 = torch.randn(4, 5, 7)
batch2 = torch.randn(4, 7, 6)
result = self_tensor.baddbmm_(batch1, batch2, beta=1, alpha=1)