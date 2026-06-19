import torch

# Prepare valid input data
input_tensor = torch.randn(5, 5)
n = None
dim = -1
norm = 'backward'
out = None

# Call the API
result = torch.fft.fft(input=input_tensor, n=n, dim=dim, norm=norm, out=out)