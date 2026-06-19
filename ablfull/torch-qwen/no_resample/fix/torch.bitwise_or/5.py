import torch
input_tensor = torch.tensor([1, 2, 3], dtype=torch.int32)
other_tensor = torch.tensor([4, 5, 6], dtype=torch.int32)
result = torch.bitwise_or(input_tensor, other_tensor)