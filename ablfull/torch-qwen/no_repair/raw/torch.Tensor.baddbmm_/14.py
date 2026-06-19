import torch

# Prepare valid input data
batch1 = torch.randn(3, 4, 5)
batch2 = torch.randn(3, 5, 6)
beta = 1
alpha = 1

# Call the API
result = torch.zeros(3, 4, 6)
result.baddbmm_(batch1, batch2, beta=beta, alpha=alpha)