
import torch
x = torch.randn(4, 4)
n = None
dim = (- 1)
norm = 'backward'
result = torch.fft.fft(x, n=n, dim=dim, norm=norm)
