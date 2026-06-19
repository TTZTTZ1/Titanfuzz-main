import torch
input_tensor = torch.randn(1, 1, 3, 4)
input_tensor.squeeze_(dim=0)