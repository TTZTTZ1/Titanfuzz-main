
import torch
input_tensor = torch.tensor([[1, 2], [4, 3]])
result = input_tensor.cummin(dim=1)
