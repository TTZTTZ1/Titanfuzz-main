
import torch
batch1 = torch.randn(2, 3, 4)
batch2 = torch.randn(2, 4, 5)
self_tensor = torch.randn(2, 3, 5)
result = self_tensor.baddbmm_(batch1, batch2, beta=1, alpha=1)
