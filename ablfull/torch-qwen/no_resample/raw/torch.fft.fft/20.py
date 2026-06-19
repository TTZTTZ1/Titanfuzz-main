import torch

# Prepare valid input data
x = torch.randn(4, 5)
dim = 1

# Call the API
result = torch.fft.fft(x, dim=dim)