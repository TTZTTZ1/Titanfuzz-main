import torch
input_tensor = torch.randn(1, 2, 1)
result = input_tensor.squeeze_(dim=0)
print(result)