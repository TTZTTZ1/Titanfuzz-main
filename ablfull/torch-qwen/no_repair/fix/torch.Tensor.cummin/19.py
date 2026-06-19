
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
dim = 0
result = input_tensor.cummin(dim)
