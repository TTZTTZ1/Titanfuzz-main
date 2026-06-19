import torch

n = 64
d = 0.5
dtype = torch.float32

result = torch.fft.rfftfreq(n, d=d, dtype=dtype)