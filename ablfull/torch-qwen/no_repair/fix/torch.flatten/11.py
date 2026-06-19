
import torch
input_tensor = torch.randn(3, 4)
flattened_tensor = torch.flatten(input_tensor, start_dim=0, end_dim=(- 1))
