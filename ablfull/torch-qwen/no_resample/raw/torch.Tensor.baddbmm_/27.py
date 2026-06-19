import torch

# Prepare input data
batch1 = torch.randn(3, 4, 5)
batch2 = torch.randn(3, 5, 6)
alpha = 1.0
beta = 1.0

# Create a tensor to hold the result
result = torch.zeros(3, 4, 6)

# Call the API
result.baddbmm_(batch1, batch2, beta=beta, alpha=alpha)