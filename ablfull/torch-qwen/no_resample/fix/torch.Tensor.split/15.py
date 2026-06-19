import torch
tensor = torch.randn(10, 5)
split_result = tensor.split(split_size=2, dim=0)