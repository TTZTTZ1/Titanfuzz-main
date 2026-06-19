import torch
data = torch.tensor([4, 1, 2, 8, 5])
sorted_indices = data.argsort()
print(sorted_indices)