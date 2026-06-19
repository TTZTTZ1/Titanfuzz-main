import torch
input_data = torch.randn(4, 5)
result = torch.fft.fft(input_data)