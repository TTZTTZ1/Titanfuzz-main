import torch
input_tensor = torch.randn(1, 10)
result = input_tensor.squeeze_()
print(result)