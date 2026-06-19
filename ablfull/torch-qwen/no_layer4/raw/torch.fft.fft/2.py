import torch

# Prepare valid input data
x = torch.randn(4, 4)

# Call the API
result = torch.fft.fft(x, dim=0)