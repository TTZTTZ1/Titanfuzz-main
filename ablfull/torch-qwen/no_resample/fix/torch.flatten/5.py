import torch
input_tensor = torch.randn(2, 3, 4)
flattened_tensor = torch.flatten(input_tensor, start_dim=1, end_dim=(- 1))
print(flattened_tensor)