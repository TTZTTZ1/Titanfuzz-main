import torch
input_tensor = torch.tensor([1, 0, 1], dtype=torch.int)
other_tensor = torch.tensor([0, 1, 0], dtype=torch.int)
result = torch.bitwise_or(input_tensor, other_tensor)