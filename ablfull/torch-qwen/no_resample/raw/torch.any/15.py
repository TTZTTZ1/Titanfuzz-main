import torch

input_tensor = torch.tensor([[False, True], [False, False]])
dim = 1
keepdim = False

result = torch.any(input_tensor, dim=dim, keepdim=keepdim)