import torch

# Create a random complex tensor
x = torch.randn(8, 4) + 1j * torch.randn(8, 4)

# Compute the 1D discrete Fourier transform
result = torch.fft.fft(x, n=16, dim=0, norm="ortho")

print(result)