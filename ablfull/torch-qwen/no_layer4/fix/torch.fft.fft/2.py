import torch
x = torch.randn(4, 4)
result = torch.fft.fft(x, dim=0)