
import torch
input_tensor = ((torch.rand((2, 2)) * 2) - 1)
result = torch.slogdet(input_tensor)
