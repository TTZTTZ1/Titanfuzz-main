import torch
input_data = torch.randn(3, 3)
result = torch.slogdet(input_data)
print(result)