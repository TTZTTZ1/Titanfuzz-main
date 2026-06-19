import torch

# Create a random complex tensor
x = torch.randn(8, 8, dtype=torch.complex64)

# Compute the N-dimensional FFT over all dimensions
xfft = torch.fft.fftn(x, norm='ortho')

print(xfft)