import torch
tensor = torch.zeros((5, 5))
sparsity = 0.2
std = 0.1
generator = torch.Generator().manual_seed(0)
result = torch.nn.init.sparse_(tensor, sparsity, std, generator)