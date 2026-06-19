import torch

# Prepare valid input data
x = torch.randn(5)
n = None
dim = -1
norm = 'backward'
out = None

# Call the target API
result = torch.fft.fft(x, n, dim, norm, out)