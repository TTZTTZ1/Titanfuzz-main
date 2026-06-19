import torch
input_data = torch.randn(5)
dim = 0
result = torch.fft.fft(input_data, dim=dim)