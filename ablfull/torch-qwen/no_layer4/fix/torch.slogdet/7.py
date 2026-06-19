import torch
input_tensor = torch.randn(3, 3)
result = torch.slogdet(input_tensor)
print(result)