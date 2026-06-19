import torch
data = torch.tensor([[1, 2], [3, 4]])
repeats = torch.tensor([2, 3])
output = torch.repeat_interleave(data, repeats, dim=0)