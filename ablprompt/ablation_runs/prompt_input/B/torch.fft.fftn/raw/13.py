import torch

# Create a random complex tensor
x = torch.randn(4, 4, 4, dtype=torch.complex64)

# Compute the N-dimensional FFT over all dimensions with normalization
fftn_result = torch.fft.fftn(x, norm="ortho")

print(fftn_result)