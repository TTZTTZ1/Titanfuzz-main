
import torch
tensor = torch.randn(1, 2, 1)
result = tensor.squeeze_(dim=0)
