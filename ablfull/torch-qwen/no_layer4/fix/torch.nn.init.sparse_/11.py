import torch
tensor = torch.randn(3, 4)
sparsity = 0.5
std = 0.1
generator = torch.Generator().manual_seed(0)
result = torch.nn.init.sparse_(tensor, sparsity, std, generator)