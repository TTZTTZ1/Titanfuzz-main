import torch
input_data = torch.tensor([4, 3, 1, 2])
sorted_indices = input_data.argsort()
print(sorted_indices)