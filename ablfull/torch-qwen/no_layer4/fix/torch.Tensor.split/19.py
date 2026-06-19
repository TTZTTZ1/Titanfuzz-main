import torch
tensor = torch.randn(4, 5)
result = tensor.split(split_size=[2, 2], dim=0)