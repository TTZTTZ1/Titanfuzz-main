import torch

# Generate input data
a = torch.randn(4, 5, 6)
b = torch.randn(4, 6, 7)
c = torch.randn(4, 5, 7)

# Call the API
result = a.baddbmm_(beta=1, alpha=1, batch1=b, batch2=c)