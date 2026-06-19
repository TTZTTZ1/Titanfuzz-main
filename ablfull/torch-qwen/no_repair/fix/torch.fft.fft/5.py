
import torch
input_tensor = torch.randn(4, 5)
dim = 1
result = torch.fft.fft(input_tensor, dim=dim)
