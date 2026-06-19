import torch

# Create a random complex tensor
x = torch.randn(8, 4, dtype=torch.complex64)

# Compute the 1D FFT along dimension 0
y = torch.fft.fft(x, n=16, dim=0, norm='ortho')

print(y)