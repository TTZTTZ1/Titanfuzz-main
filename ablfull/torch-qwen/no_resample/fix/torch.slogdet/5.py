import torch
n = 4
input_data = torch.randn(n, n)
result = torch.slogdet(input_data)
print(result)