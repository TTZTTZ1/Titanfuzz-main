
import torch
tensor = torch.randn(10)
result = tensor.split(split_size=[4, 6], dim=0)
