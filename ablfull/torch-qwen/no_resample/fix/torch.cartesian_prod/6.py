import torch
tensor1 = torch.tensor([1, 2], dtype=torch.float)
tensor2 = torch.tensor([3, 4], dtype=torch.float)
result = torch.cartesian_prod(tensor1, tensor2)
print(result)