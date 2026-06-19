import torch

N = 512
dN = 0.1
frequencies = torch.fft.rfftfreq(N, d=dN)
print(frequencies)