import torch
tensor = torch.randn(1, 1, 2, 2)
result = tensor.squeeze_(dim=0)