import torch

# Prepare input data
input_tensor = torch.randn(4, 5)
dim = 1

# Call the API
result = torch.fft.fft(input=input_tensor, dim=dim)