import torch
tensor = torch.tensor([3, 1, 4, 1, 5, 9, 2, 6])
sorted_indices = tensor.argsort(dim=0)
print(sorted_indices)