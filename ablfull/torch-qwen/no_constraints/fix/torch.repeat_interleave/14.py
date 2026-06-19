import torch
input_tensor = torch.tensor([[1, 2], [3, 4]])
repeats = 3
output = torch.repeat_interleave(input_tensor, repeats)