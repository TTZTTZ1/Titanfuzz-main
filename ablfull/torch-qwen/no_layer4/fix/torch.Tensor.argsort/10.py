import torch
input_tensor = torch.tensor([[1, 0, 2], [3, 4, 5]])
sorted_indices = input_tensor.argsort(dim=1)
print(sorted_indices)