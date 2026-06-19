import torch
tensor = torch.tensor([4, 1, 3, 2])
sorted_indices = tensor.argsort(dim=0, descending=False)
print(sorted_indices)