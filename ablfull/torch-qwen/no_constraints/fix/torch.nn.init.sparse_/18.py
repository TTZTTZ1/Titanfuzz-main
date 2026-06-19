import torch
tensor = torch.empty(3, 4)
sparsity = 0.5
result = torch.nn.init.sparse_(tensor, sparsity)
print(result)