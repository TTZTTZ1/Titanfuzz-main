import torch
input_tensor = torch.randn(3, 4, 5)
result = torch.flatten(input_tensor, start_dim=1, end_dim=(- 1))