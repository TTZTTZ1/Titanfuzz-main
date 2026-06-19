import torch
input_tensor = torch.randn(1, 1, 2, 2)
input_tensor.squeeze_(dim=0)
print(input_tensor.shape)