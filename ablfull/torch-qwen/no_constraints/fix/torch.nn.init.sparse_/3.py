import torch
tensor = torch.zeros(5, 5)
sparsity = 0.7
std = 0.01
result = torch.nn.init.sparse_(tensor, sparsity, std)