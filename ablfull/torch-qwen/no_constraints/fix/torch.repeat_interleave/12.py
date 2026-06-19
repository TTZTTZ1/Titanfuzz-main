import torch
input_tensor = torch.tensor([1, 2, 3], dtype=torch.long)
repeats = torch.tensor([2, 2, 2], dtype=torch.long)
result = torch.repeat_interleave(input_tensor, repeats)
print(result)