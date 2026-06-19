
import torch
tensor = torch.randn(3, 4)
dims = (1, 0)
result = tensor.permute(dims)
print(result)
