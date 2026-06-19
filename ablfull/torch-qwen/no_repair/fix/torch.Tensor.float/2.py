
import torch
input_tensor = torch.randn(3, 4)
result = input_tensor.float(memory_format=torch.preserve_format)
