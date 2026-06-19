import torch
batch1 = torch.randn(3, 4, 5)
batch2 = torch.randn(3, 5, 6)
beta = 2
alpha = 3
result_tensor = torch.randn(3, 4, 6)
result_tensor.baddbmm_(batch1, batch2, beta=beta, alpha=alpha)