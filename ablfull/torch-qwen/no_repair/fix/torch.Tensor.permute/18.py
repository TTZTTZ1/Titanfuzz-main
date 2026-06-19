
import torch
tensor = torch.randn(2, 3, 4)
permuted_tensor = tensor.permute((2, 0, 1))
print(permuted_tensor)
