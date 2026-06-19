import torch
data = torch.tensor([4, 3, 1, 2])
sorted_indices = data.argsort()
print(sorted_indices)