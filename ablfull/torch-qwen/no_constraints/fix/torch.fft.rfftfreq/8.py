import torch
n = 5
d = 0.1
result = torch.fft.rfftfreq(n, d)
print(result)