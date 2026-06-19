import torch
tensor = torch.zeros(4, 5)
sparsity = 0.5
result = torch.nn.init.sparse_(tensor, sparsity)