
import torch
input_tensor = torch.randn(4, 5)
result = torch.transpose(input_tensor, dim0=0, dim1=1)
