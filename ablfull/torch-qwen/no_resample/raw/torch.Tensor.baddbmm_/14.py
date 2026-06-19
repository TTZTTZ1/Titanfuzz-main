import torch

# Prepare valid input data
batch1 = torch.randn(3, 4, 5)
batch2 = torch.randn(3, 5, 6)
alpha = 2
beta = 0.5

# Call the API
result = torch.randn(3, 4, 6).baddbmm_(batch1, batch2, beta=beta, alpha=alpha)
print(result)