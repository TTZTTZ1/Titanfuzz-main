import torch

# Prepare valid input data
input_tensor = torch.randn(4, 5)
n = None
dim = 0
norm = 'backward'
out = None

# Call the target API
result = torch.fft.fft(input_tensor, n=n, dim=dim, norm=norm, out=out)