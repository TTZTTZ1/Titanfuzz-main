import torch

data = torch.tensor([[1, 2], [3, 4]])
repeats = 2
result = torch.repeat_interleave(data, repeats)