import torch

data = torch.randn(3, 4)
result = data.float(memory_format=torch.channels_last)