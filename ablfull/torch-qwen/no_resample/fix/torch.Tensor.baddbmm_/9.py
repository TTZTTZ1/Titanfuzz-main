import torch
batch1 = torch.randn(3, 4, 5)
batch2 = torch.randn(3, 5, 6)
alpha = 1.0
beta = 1.0
result = torch.zeros(3, 4, 6)
result.baddbmm_(batch1, batch2, beta=beta, alpha=alpha)