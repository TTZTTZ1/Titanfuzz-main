import torch

# Create sample tensors that satisfy the constraints
self_tensor = torch.randn(2, 3, 4)
batch1 = torch.randn(2, 5, 4)
batch2 = torch.randn(2, 4, 6)

# Prepare beta and alpha scalars
beta = 2.0
alpha = 1.5

# Call the API
result = self_tensor.baddbmm_(batch1, batch2, beta=beta, alpha=alpha)