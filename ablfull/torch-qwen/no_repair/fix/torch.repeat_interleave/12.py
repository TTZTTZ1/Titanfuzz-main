
import torch
input_tensor = torch.tensor([1, 2, 3])
repeats = torch.tensor(2)
dim = 0
result = torch.repeat_interleave(input_tensor, repeats, dim=dim)
print(result)
