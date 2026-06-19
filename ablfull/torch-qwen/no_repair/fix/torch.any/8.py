
import torch
input_tensor = torch.tensor([[0, 1], [2, 0]])
dim = 1
result = torch.any(input_tensor, dim=dim)
