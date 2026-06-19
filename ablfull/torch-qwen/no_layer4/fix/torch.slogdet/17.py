import torch
input_data = torch.randn(5, 5)
result = torch.slogdet(input_data)
print(result)