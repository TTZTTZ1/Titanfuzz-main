import torch

# Create a random complex tensor
x = torch.randn(8, 8, dtype=torch.complex64)

# Compute the N-dimensional FFT over all dimensions
fftn_result = torch.fft.fftn(x)

print(fftn_result)