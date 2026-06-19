
import torch
data = torch.randn(2, 3, 4)
dims = (0, 2, 1)
result = data.permute(dims)
