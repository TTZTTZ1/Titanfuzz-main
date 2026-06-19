import torch
input_tensor = torch.randn(4, 4)
result = torch.slogdet(input_tensor)