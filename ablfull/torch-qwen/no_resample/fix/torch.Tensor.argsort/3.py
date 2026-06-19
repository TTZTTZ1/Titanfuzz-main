import torch
input_tensor = torch.tensor([4, 2, 3, 1])
sorted_indices = input_tensor.argsort(dim=0, descending=False)
print(sorted_indices)