import torch

# Create a complex tensor
x = torch.randn(8, 8, dtype=torch.complex64)

# Compute the N-dimensional FFT
fftn_result = torch.fft.fftn(x, s=(4, 4), dim=(-2, -1), norm='ortho')

print(fftn_result)