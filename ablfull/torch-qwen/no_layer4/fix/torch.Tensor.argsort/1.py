import torch
input_tensor = torch.tensor([[10, 5, 8], [3, 7, 2]])
sorted_indices = input_tensor.argsort(dim=1, descending=True)
print(sorted_indices)