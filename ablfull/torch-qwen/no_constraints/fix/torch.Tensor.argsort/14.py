import torch
input_data = torch.tensor([[4, 3, 1], [2, 5, 6]])
sorted_indices = input_data.argsort(dim=1)
print(sorted_indices)