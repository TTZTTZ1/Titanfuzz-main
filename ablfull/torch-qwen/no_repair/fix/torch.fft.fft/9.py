
import torch
input_tensor = torch.randn(4, 4)
dim = 0
result = torch.fft.fft(input=input_tensor, dim=dim, norm='backward')
