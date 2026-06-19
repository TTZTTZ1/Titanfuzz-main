
import torch
x = torch.tensor([[[0, 1], [2, 3]], [[4, 5], [6, 7]]])
result = torch.fft.fft(x, dim=1, norm='backward')
