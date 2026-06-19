import torch

# Prepare valid input data
a = torch.randn(2, 3, 4)
b = torch.randn(2, 4, 5)
c = torch.randn(2, 3, 5)

# Call the API
result = a.baddbmm_(beta=1, alpha=1, batch1=b, batch2=c)