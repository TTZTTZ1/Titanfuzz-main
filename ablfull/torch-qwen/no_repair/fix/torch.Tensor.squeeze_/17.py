
import torch
tensor = torch.randn(1, 3, 1, 4)
result = tensor.squeeze_(dim=0)
