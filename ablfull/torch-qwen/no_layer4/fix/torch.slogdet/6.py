import torch
input_tensor = ((torch.rand((3, 3)) * 2) - 1)
result = torch.slogdet(input_tensor)