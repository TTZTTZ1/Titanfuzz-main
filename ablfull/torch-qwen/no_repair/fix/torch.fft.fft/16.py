
import torch
x = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
result = torch.fft.fft(x, dim=1)
