import torch

# Create a random complex tensor
x = torch.randn(8, 4) + 1j * torch.randn(8, 4)

# Compute the 1D FFT along dimension 0 with normalization
result = torch.fft.fft(x, dim=0, norm='ortho')

print(result)