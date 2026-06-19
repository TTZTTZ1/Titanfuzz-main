import torch
tensor1 = torch.tensor([])
tensor2 = torch.tensor([1, 2, 3])
tensors = [tensor1, tensor2]
dim = 0
result = torch.cat(tensors, dim)
print(result)