import torch
n = 50
d = 0.1
freqs = torch.fft.rfftfreq(n, d)
print(freqs)