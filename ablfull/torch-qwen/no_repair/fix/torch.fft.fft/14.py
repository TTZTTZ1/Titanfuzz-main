
import torch
input_tensor = torch.randn(4, 5)
n = None
dim = 0
norm = 'backward'
result = torch.fft.fft(input_tensor, n=n, dim=dim, norm=norm)
