import torch

# Initialize tensors that meet the required dimensions and shapes
tensor = torch.randn(5, 3, 4)
batch1 = torch.randn(5, 3, 6)
batch2 = torch.randn(5, 6, 8)

# Define the parameters
beta = 0.5
alpha = 2.0

# Call the API
tensor.baddbmm_(batch1, batch2, beta=beta, alpha=alpha)