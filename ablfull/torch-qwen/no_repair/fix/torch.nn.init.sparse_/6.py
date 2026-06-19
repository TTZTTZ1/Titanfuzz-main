
import torch
tensor = torch.randn(5, 5)
sparsity = 0.5
std = 0.1
result = torch.nn.init.sparse_(tensor, sparsity, std=std)
print(result)
