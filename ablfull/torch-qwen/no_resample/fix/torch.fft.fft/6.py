import torch
x = torch.randn(4, 4)
n = None
dim = 0
norm = 'backward'
out = None
result = torch.fft.fft(x, n=n, dim=dim, norm=norm, out=out)