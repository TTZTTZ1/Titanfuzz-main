import torch
tensor1 = torch.tensor([1, 2])
tensor2 = torch.tensor([5, 6])
result = torch.cartesian_prod(tensor1, tensor2)
print(result)