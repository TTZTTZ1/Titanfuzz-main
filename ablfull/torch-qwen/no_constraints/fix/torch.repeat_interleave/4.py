import torch
input_tensor = torch.tensor([1, 2, 3])
repeats = 2
output_tensor = torch.repeat_interleave(input_tensor, repeats)
print(output_tensor)