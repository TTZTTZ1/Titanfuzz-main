import torch
tensor1 = torch.tensor([1, 2, 3])
tensor2 = torch.tensor([4, 5])
result = torch.cartesian_prod(tensor1, tensor2)
print(result)