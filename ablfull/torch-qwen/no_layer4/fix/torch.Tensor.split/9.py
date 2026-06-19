import torch
tensor = torch.randn(10)
split_tensors = tensor.split(split_size=[3, 4, 3], dim=0)