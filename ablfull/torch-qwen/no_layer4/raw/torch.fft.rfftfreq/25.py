import torch

n = 5
d = 1.0
out = None
dtype = None
layout = torch.strided
device = None
requires_grad = False

result = torch.fft.rfftfreq(n, d, out, dtype, layout, device, requires_grad)