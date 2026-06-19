import torch
input_data = torch.tensor([4, 1, 2, 3])
sorted_indices = input_data.argsort()
print(sorted_indices)