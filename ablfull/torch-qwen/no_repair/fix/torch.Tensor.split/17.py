
import torch
tensor = torch.randn(10, 4)
split_result = tensor.split([3, 7], dim=0)
