import torch

# Prepare input data
input_data = torch.randn(4, 4)
dim = 0

# Call the API
result = torch.fft.fft(input=input_data, dim=dim)