import torch

# Create a random complex tensor
x = torch.randn(4, 4, dtype=torch.complex64)

# Compute the N-dimensional discrete Fourier transform of the tensor
fftn_result = torch.fft.fftn(x, s=(3, 3), dim=(0, 1), norm='ortho')

print(fftn_result)