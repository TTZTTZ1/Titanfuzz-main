import torch
input_tensor = torch.tensor([[1, 2], [3, 4]])
repeats = torch.tensor([2, 3])
output = torch.repeat_interleave(input_tensor, repeats, dim=0)