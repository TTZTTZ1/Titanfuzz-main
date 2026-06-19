import torch
tensor = torch.tensor([4, 3, 1, 2])
sorted_indices = tensor.argsort(dim=0)
print(sorted_indices)