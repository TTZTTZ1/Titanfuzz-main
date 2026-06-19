import torch
input_tensor = torch.randn(1, 1, 3, 4)
input_tensor.squeeze_()
print(input_tensor.shape)