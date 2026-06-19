import torch

# Prepare input data
input_tensor = torch.randn(5)
dim = 0

# Call the API
result = torch.fft.fft(input=input_tensor, dim=dim)