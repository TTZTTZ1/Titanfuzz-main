import torch
input_tensor = torch.tensor([3, 1, 4, 1, 5, 9, 2, 6])
sorted_indices = input_tensor.argsort()
print(sorted_indices)