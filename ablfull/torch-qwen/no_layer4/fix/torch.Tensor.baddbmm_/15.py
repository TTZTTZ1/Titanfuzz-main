import torch
batch1 = torch.randn(4, 5, 6)
batch2 = torch.randn(4, 6, 7)
result_tensor = torch.randn(4, 5, 7)
result_tensor.baddbmm_(batch1, batch2, beta=1, alpha=1)