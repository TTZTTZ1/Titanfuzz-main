import torch
tensor = torch.randn(5, 5)
sparsity = 0.5
std = 0.1
generator = torch.Generator().manual_seed(0)
result = torch.nn.init.sparse_(tensor, sparsity, std, generator)