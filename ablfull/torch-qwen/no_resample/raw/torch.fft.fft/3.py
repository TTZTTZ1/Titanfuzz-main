import torch

# Prepare valid input data
x = torch.randn(4, 5)

# Call the API
result = torch.fft.fft(x, dim=0)