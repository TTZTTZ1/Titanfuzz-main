
import torch
self_tensor = torch.randn(5, 3, 4)
batch1 = torch.randn(5, 3, 2)
batch2 = torch.randn(5, 2, 4)
result = self_tensor.baddbmm_(beta=1, alpha=1, batch1=batch1, batch2=batch2)
