import torch
input_tensor = torch.randn(4, 5)
dim = 0
result = torch.fft.fft(input=input_tensor, dim=dim)