
import torch
tensor = torch.randn(10)
split_tensors = tensor.split(split_size=5, dim=0)
