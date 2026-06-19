import torch

input_tensor = torch.tensor([[0, 0], [0, 1]])
dim = 1
keepdim = True

result = torch.any(input_tensor, dim=dim, keepdim=keepdim)