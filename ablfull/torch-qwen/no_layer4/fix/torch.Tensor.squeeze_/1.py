import torch
input_tensor = torch.randn(1, 3, 1)
input_tensor.squeeze_(dim=0)