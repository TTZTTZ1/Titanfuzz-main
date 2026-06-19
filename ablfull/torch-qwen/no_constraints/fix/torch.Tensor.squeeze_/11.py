import torch
input_tensor = torch.randn(1, 3, 1, 4)
result_tensor = input_tensor.squeeze_()
print(result_tensor)