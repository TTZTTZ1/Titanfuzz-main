
import torch
input_tensor = torch.tensor([4, 2, 5, 1])
sorted_indices = input_tensor.argsort(dim=0)
print(sorted_indices)
