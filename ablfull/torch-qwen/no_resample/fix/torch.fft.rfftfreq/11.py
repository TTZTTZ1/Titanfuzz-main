import torch
n = 5
d = 1.0
out = None
dtype = torch.float32
layout = torch.strided
device = torch.device('cpu')
requires_grad = False
result = torch.fft.rfftfreq(n=n, d=d, out=out, dtype=dtype, layout=layout, device=device, requires_grad=requires_grad)