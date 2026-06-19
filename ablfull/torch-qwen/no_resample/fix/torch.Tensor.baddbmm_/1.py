import torch
self_tensor = torch.randn(2, 3, 4)
batch1_tensor = torch.randn(2, 3, 5)
batch2_tensor = torch.randn(2, 5, 4)
result = self_tensor.baddbmm_(batch1=batch1_tensor, batch2=batch2_tensor, beta=1, alpha=1)