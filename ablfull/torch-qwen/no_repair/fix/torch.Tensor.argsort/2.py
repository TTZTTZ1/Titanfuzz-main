
import torch
input_tensor = torch.tensor([[10, 50, 30], [60, 20, 40]])
sorted_indices = input_tensor.argsort(dim=1, descending=True)
print(sorted_indices)
