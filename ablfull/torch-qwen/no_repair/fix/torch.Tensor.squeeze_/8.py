
import torch
input_tensor = torch.randn(1, 1, 5)
result = input_tensor.squeeze_(dim=0)
