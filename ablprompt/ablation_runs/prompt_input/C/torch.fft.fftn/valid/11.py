import torch

# Create a random complex tensor
x = torch.randn(4, 4, 4, dtype=torch.complex64)

# Compute the N-dimensional FFT over all dimensions
xfft_result = torch.fft.fftn(x)

print(xfft_result)