import torch
input_data = torch.tensor([3, 1, 4, 1, 5, 9], dtype=torch.int)
sorted_indices = torch.argsort(input_data)
print(sorted_indices)