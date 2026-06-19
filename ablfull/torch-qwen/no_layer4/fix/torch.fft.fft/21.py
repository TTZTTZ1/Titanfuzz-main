import torch
input_tensor = torch.randn(5, 4)
dim = 1
result = torch.fft.fft(input=input_tensor, dim=dim)