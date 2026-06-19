import torch
N = 64
dN = 0.5
result = torch.fft.rfftfreq(N, d=dN)
print(result)