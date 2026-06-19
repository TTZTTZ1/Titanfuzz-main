import torch
n = 64
d = 0.1
dtype = torch.float32
result = torch.fft.rfftfreq(n, d=d, dtype=dtype)
print(result)