
import torch
input_tensor = torch.tensor([[10, 5, 3], [8, 2, 9]])
sorted_indices = input_tensor.argsort(dim=1, descending=True)
print(sorted_indices)
