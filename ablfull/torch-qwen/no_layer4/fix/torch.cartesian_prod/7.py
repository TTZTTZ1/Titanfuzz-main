import torch
tensors = [torch.tensor([1, 2, 3]), torch.tensor([4, 5])]
result = torch.cartesian_prod(*tensors)
print(result)