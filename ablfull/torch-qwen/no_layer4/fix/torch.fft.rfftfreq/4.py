import torch
n = 10
d = 1.0
dtype = torch.float32
result = torch.fft.rfftfreq(n=n, d=d, dtype=dtype)