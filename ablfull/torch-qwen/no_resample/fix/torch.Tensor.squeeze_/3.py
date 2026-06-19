import torch
input_tensor = torch.randn(1, 1, 3, 4)
result = input_tensor.squeeze_()
print(result)