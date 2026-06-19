
import torch
input_data = torch.randn(4, 4)
dim = 0
result = torch.fft.fft(input=input_data, dim=dim)
