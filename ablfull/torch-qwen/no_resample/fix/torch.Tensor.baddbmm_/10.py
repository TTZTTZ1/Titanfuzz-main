import torch
batch1 = torch.randn(3, 4, 5)
batch2 = torch.randn(3, 5, 6)
alpha = 2
beta = 1
result = torch.zeros(3, 4, 6)
result.baddbmm_(batch1, batch2, beta=beta, alpha=alpha)