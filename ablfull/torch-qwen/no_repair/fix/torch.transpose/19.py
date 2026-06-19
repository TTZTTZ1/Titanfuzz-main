
import torch
x = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
result = torch.transpose(x, 0, 1)
