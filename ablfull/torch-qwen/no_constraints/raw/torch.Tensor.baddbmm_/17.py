import torch

# Generate input data
batch1 = torch.randn(2, 3)
batch2 = torch.randn(2, 4)
batch3 = torch.randn(2, 3, 4)

# Call the API
result = batch1.baddbmm_(batch2, batch3)