import torch
x = torch.tensor([1, 2, 3], dtype=torch.float32)
result = torch.fft.fft(x, dim=0)