import torch

# Generate input data
batch1 = torch.randn(5, 4, 3)
batch2 = torch.randn(5, 3, 6)

# Prepare valid input for the API
beta = 2.0
alpha = 3.0

# Call the API
result = torch.tensor([[1.0] * 6] * 5)  # Initialize with zeros to match the output shape
result.baddbmm_(batch1, batch2, beta=beta, alpha=alpha)