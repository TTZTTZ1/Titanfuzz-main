import torch
input_tensor = torch.randn(4, 5)
dim0 = 0
dim1 = 1
result = torch.transpose(input_tensor, dim0, dim1)