import torch

# Prepare valid input data
input_tensor = torch.randn(5, 4)
dim = 1

# Call the API
result = torch.fft.fft(input=input_tensor, dim=dim)