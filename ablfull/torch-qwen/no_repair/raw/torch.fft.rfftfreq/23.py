import torch

n = 5
d = 1.0
dtype = torch.float32

result = torch.fft.rfftfreq(n, d=d, dtype=dtype)