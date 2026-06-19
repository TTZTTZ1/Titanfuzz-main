import torch
tensor = torch.zeros(4, 5)
sparsity = 0.8
std = 0.01
result_tensor = torch.nn.init.sparse_(tensor, sparsity, std)