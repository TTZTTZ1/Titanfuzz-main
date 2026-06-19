import torch
x = torch.tensor([0.5, 0.2, 0.8, 0.4], dtype=torch.float32)
result = torch.fft.fft(x)