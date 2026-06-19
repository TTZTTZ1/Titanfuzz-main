import torch
input_data = torch.randn(3, 3, dtype=torch.double)
result = torch.slogdet(input_data)
print(result)