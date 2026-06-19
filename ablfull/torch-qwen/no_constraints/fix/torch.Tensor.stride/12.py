import torch
data = torch.randn(4, 5)
result = data.stride()
print(result)