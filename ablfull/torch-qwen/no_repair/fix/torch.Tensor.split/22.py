
import torch
data = torch.randn(10)
result = data.split(split_size=[3, 4, 3], dim=0)
