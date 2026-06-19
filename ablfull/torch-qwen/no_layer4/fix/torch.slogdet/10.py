import torch
n = 4
input_tensor = torch.randn(n, n)
result = torch.slogdet(input_tensor)