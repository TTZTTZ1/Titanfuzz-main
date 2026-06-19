import torch
data = torch.tensor([3, 1, 4, 1, 5, 9, 2])
sorted_indices = data.argsort()
print(sorted_indices)