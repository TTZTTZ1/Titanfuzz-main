
import torch
x = torch.randn(4, 5)
n = None
dim = (- 1)
norm = 'backward'
out = None
result = torch.fft.fft(x, n=n, dim=dim, norm=norm, out=out)
