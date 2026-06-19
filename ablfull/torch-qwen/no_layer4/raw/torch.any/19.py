import torch

input_tensor = torch.tensor([[True, False], [False, True]])
dim = 1
keepdim = True

result = torch.any(input_tensor, dim=dim, keepdim=keepdim)