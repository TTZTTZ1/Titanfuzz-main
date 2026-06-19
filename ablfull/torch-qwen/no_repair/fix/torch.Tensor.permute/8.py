
import torch
data = torch.randn(2, 3, 4)
dims = (1, 0, 2)
result = data.permute(dims)
