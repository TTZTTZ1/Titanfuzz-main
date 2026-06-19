import torch

# Prepare valid input data
tensor_self = torch.randn(3, 4, 5)
batch1 = torch.randn(3, 4, 6)
batch2 = torch.randn(3, 6, 5)

# Call the API
tensor_self.baddbmm_(batch1, batch2, beta=1, alpha=1)