import torch
n = 50
d = 1
result = torch.fft.rfftfreq(n, d)
print(result)