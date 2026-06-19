import torch
input_tensor = torch.randn(4, 4)
(dim0, dim1) = (0, 1)
result = torch.transpose(input_tensor, dim0, dim1)