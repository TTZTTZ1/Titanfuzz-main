import torch
input_tensor = torch.randn(2, 2)
input_tensor = input_tensor.float()
result = torch.slogdet(input_tensor)
print(result)