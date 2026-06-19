import torch
input_data = torch.tensor([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
sorted_indices = input_data.argsort()
print(sorted_indices)