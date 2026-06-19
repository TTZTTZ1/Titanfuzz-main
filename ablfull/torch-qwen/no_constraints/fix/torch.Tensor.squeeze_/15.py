import torch
input_tensor = torch.randn(1, 1, 2, 2)
result_tensor = input_tensor.squeeze_()
print(result_tensor)