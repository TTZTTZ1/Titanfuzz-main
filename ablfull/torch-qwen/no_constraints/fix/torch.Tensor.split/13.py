import torch
tensor = torch.randn(10, 5)
split_tensors = tensor.split(split_size=2, dim=0)