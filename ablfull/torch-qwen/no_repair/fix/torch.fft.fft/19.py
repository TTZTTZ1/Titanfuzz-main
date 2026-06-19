
import torch
input_data = torch.randn(4, 5)
dim = 1
result = torch.fft.fft(input_data, dim=dim, norm='backward')
