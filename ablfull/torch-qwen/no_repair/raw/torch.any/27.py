import torch

input_tensor = torch.tensor([[True, False], [False, True]])
dim = (0, 1)
result = torch.any(input=input_tensor, dim=dim, keepdim=True)