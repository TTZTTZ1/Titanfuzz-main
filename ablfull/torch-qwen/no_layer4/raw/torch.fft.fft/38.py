import torch

# Prepare input data
input_tensor = torch.randn(5, 3)

# Call the API
result = torch.fft.fft(input_tensor, n=None, dim=-1, norm='backward')