import torch
tensor = torch.randn(5, 5)
sparsity = 0.3
std = 0.1
result = torch.nn.init.sparse_(tensor, sparsity, std)