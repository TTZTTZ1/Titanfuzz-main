import torch

# Prepare input data
input_tensor = torch.randn(4, 4)
dim = 0

# Call the API
result = torch.fft.fft(input_tensor, dim=dim)