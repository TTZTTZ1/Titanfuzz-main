import torch
x = torch.randn(2, 3)
(dim0, dim1) = (0, 1)
result = torch.transpose(x, dim0, dim1)