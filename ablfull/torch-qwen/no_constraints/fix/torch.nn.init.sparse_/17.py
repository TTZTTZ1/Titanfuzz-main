import torch
tensor = torch.zeros(4, 5)
sparsity = 0.75
std = 0.01
result = torch.nn.init.sparse_(tensor, sparsity, std)