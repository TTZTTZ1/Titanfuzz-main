import torch

input_tensor = torch.tensor([0.0, 1.0], dtype=torch.float32)
other_tensor = torch.tensor([1.0, 0.0], dtype=torch.float32)

result = torch.atan2(input_tensor, other_tensor)