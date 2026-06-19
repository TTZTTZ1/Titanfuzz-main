import torch
x = torch.randn(4, 5)
dim = 1
result = torch.fft.fft(x, dim=dim)