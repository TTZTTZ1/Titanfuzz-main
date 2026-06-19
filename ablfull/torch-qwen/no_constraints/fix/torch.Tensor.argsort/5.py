import torch
input_tensor = torch.tensor([4, 1, 2, 3])
sorted_indices = input_tensor.argsort()
print(sorted_indices)