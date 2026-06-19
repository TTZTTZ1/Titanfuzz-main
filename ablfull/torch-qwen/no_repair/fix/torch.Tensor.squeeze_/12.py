
import torch
input_tensor = torch.randn(1, 1, 2, 3)
input_tensor.squeeze_(dim=0)
