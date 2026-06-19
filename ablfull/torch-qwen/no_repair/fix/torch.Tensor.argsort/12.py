
import torch
input_tensor = torch.tensor([[1, 3, 2]])
sorted_indices = input_tensor.argsort(dim=1)
print(sorted_indices)
