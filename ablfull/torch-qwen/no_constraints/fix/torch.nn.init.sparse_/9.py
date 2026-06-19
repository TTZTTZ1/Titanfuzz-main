import torch
tensor = torch.zeros(3, 4)
sparsity = 0.5
std = 0.01
result = torch.nn.init.sparse_(tensor, sparsity, std)
print(result)