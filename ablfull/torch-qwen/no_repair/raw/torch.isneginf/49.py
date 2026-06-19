import torch

input_data = torch.tensor([[-float('inf'), 0.5], [2.5, -float('inf')]])
result = torch.isneginf(input_data)
print(result)