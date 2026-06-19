import torch

# Create a random complex tensor
x = torch.randn(4, 4, dtype=torch.complex64)

# Compute the 2D FFT over all dimensions
fftn_result = torch.fft.fftn(x)

print(fftn_result)