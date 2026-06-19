
import torch
n = 10
d = 1.0
dtype = torch.float32
layout = torch.strided
device = torch.device('cpu')
requires_grad = False
result = torch.fft.rfftfreq(n, d=d, dtype=dtype, layout=layout, device=device, requires_grad=requires_grad)
