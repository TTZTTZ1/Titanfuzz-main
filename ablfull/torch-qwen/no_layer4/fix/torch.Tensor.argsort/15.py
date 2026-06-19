import torch
input_tensor = torch.tensor([3, 1, 4, 1, 5])
sorted_indices = input_tensor.argsort(dim=0)
print(sorted_indices)