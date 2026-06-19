import torch
data = torch.randn(3, 4)
result = data.stride()
print(result)