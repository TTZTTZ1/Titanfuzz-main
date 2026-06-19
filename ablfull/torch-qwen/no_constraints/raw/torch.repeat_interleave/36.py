import torch

input_tensor = torch.tensor([1, 2, 3], dtype=torch.long)
repeats = [2, 2, 2]
result = torch.repeat_interleave(input_tensor, repeats)
print(result)