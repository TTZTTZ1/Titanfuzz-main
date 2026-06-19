import torch

# Prepare valid input data
input_data = torch.randn(5)
dim = 0

# Call the API
result = torch.fft.fft(input_data, dim=dim)