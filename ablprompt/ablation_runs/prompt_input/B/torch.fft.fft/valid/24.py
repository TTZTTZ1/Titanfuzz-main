import torch

# Create a random complex tensor
x = torch.randn(8, 4) + 1j * torch.randn(8, 4)

# Compute the 1D FFT along dimension 1
y = torch.fft.fft(x, dim=1, norm='ortho')

print(y)