
import torch
data = torch.randn(4, 3, 64, 64)
result = data.float(memory_format=torch.channels_last)
