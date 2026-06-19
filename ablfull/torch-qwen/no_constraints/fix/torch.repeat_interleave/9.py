import torch
tensor = torch.tensor([[1, 2], [3, 4]])
repeats = 3
result = torch.repeat_interleave(tensor, repeats)
print(result)