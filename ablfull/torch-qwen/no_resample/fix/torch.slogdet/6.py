import torch
input_data = torch.randn(4, 4)
result = torch.slogdet(input_data)
print(result)