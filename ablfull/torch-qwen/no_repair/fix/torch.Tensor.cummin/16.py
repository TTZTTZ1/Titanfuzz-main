
import torch
input_tensor = torch.tensor([4, 2, 3, 1], dtype=torch.float32)
result = input_tensor.cummin(dim=0)
