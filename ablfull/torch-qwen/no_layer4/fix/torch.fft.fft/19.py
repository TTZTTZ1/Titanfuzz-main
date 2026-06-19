import torch
input_tensor = torch.randn(5, 3)
result = torch.fft.fft(input_tensor, n=None, dim=(- 1), norm='backward')