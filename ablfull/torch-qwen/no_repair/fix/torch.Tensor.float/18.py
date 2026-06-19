
import torch
input_tensor = torch.randint(0, 256, (4, 4))
result = input_tensor.float(memory_format=torch.contiguous_format)
