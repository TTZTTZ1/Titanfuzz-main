import torch
tensor = torch.zeros(3, 4)
sparsity = 0.5
std = 0.02
generator = torch.Generator().manual_seed(0)
result = torch.nn.init.sparse_(tensor, sparsity, std, generator)