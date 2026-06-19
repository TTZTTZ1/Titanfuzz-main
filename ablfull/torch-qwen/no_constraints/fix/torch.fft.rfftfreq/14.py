import torch
n = 5
d = 0.5
result = torch.fft.rfftfreq(n, d)
print(result)