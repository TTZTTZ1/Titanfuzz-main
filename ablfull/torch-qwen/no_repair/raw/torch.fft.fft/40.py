import torch

# Generate input data
input_data = torch.randn(4, 5)
dim = 1

# Call the API
result = torch.fft.fft(input_data, dim=dim, norm='backward')