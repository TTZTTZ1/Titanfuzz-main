import torch
input_tensor = torch.tensor([[1, 2, 3], [6, 5, 4]])
sorted_indices = input_tensor.argsort(dim=1, descending=False)
print(sorted_indices)