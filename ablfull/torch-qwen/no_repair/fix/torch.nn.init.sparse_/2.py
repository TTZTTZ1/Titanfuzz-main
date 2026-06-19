
import torch
tensor = torch.randn(5, 5)
sparsity = 0.2
std = 0.1
generator = None
result = torch.nn.init.sparse_(tensor, sparsity, std, generator)
