import torch

n = 8
d = 1.0

result = torch.fft.rfftfreq(n, d)
print(result)