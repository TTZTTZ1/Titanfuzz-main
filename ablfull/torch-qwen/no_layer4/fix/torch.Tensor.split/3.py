import torch
tensor = torch.randn(4, 4)
split_result = tensor.split(2, dim=0)