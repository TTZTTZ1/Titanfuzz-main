import torch

# Generate input data
batch1 = torch.randn(2, 3)
batch2 = torch.randn(2, 4, 3)
batch3 = torch.randn(2, 4)

# Call the API
result = batch3.baddbmm_(batch1, batch2)