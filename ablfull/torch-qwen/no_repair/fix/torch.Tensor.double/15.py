
import torch
input_tensor = torch.randn(5)
result = input_tensor.double(memory_format=torch.preserve_format)
