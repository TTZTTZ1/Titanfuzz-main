import torch
input_tensor = torch.randn(3, 3)
input_tensor = input_tensor.float()
result = torch.slogdet(input_tensor)
print(result)