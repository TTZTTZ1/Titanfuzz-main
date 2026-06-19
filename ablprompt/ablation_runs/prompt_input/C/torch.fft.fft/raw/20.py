import torch

# Create a random complex tensor
x = torch.randn(8, 4, 2) + 1j * torch.randn(8, 4, 2)

# Compute the FFT along dimension 1
y = torch.fft.fft(x, dim=1, norm='ortho')

print(y)