import torch
x = torch.randn(4, 5)
(dim0, dim1) = (0, 1)
result = torch.transpose(x, dim0, dim1)