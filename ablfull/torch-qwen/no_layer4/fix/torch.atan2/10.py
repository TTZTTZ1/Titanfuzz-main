import torch
input_data = torch.tensor([1.0, 2.0], dtype=torch.float32)
other_data = torch.tensor([0.5, 1.0], dtype=torch.float32)
result = torch.atan2(input_data, other_data)