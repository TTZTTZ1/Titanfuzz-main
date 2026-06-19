import torch

n = 64
d = 1.0
dtype = torch.float32

result = torch.fft.rfftfreq(n=n, d=d, dtype=dtype)