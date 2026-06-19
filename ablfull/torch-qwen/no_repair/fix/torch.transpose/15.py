
import torch
input_tensor = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
dim0 = 0
dim1 = 1
result = torch.transpose(input_tensor, dim0, dim1)
