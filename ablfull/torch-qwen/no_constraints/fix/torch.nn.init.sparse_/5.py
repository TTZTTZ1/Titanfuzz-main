import torch
tensor = torch.zeros(4, 4)
sparsity = 0.5
std = 0.01
result = torch.nn.init.sparse_(tensor, sparsity, std)
print(result)