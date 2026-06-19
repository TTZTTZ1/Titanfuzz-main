import torch

# Create a complex tensor
x = torch.randn(4, 4, dtype=torch.complex64)

# Compute the N-dimensional discrete Fourier transform
fftn_result = torch.fft.fftn(x, s=(8, 8), dim=(0, 1), norm="ortho")

print(fftn_result)