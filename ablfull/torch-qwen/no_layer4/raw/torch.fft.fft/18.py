import torch

# Prepare valid input data
x = torch.randn(4, 5)
n = None
dim = -1
norm = 'backward'
out = None

# Call the API
result = torch.fft.fft(x, n=n, dim=dim, norm=norm, out=out)