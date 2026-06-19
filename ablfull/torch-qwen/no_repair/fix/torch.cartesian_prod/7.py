
import torch
tensors = [torch.tensor([1, 2]), torch.tensor([3, 4])]
result = torch.cartesian_prod(*tensors)
