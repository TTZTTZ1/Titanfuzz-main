import torch

# Prepare valid input data
x = torch.randn(4, 4)
n = None
dim = -1
norm = 'backward'

# Call the API
result = torch.fft.fft(x, n=n, dim=dim, norm=norm)