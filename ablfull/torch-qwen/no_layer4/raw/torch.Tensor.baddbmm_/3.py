import torch

# Prepare valid input data
batch1 = torch.randn(3, 4, 5)
batch2 = torch.randn(3, 5, 6)
beta = 2
alpha = 3

# Create a tensor to call baddbmm_ on
result_tensor = torch.randn(3, 4, 6)

# Call the API
result_tensor.baddbmm_(batch1, batch2, beta=beta, alpha=alpha)