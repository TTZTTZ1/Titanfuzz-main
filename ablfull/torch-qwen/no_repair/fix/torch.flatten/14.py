
import torch
input_tensor = torch.randn(2, 3, 4)
result = torch.flatten(input_tensor, start_dim=1, end_dim=2)
