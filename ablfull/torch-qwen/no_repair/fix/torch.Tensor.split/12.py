
import torch
tensor = torch.randn(10, 5)
result = tensor.split(2, dim=1)
