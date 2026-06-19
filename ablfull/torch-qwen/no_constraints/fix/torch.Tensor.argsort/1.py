import torch
input_tensor = torch.tensor([4, 2, 5, 1, 3])
sorted_indices = input_tensor.argsort()
print(sorted_indices)