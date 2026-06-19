import torch
input_tensor = torch.randn(1, 2, 1)
input_tensor.squeeze_(dim=0)
print(input_tensor)