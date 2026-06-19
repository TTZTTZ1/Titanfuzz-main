
import torch
self_tensor = torch.randn(4, 5, 6)
batch1_tensor = torch.randn(4, 5, 7)
batch2_tensor = torch.randn(4, 7, 6)
self_tensor.baddbmm_(batch1=batch1_tensor, batch2=batch2_tensor, beta=1, alpha=1)
