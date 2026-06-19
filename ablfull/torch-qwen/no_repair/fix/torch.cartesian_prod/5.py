
import torch
t1 = torch.tensor([1, 2])
t2 = torch.tensor([3, 4])
result = torch.cartesian_prod(t1, t2)
print(result)
