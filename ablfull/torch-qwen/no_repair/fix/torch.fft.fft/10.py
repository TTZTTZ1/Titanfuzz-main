
import torch
x = torch.randn(4, 5)
result = torch.fft.fft(x, dim=0)
