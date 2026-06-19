import torch

# Create a random complex tensor
x = torch.randn(8, 4, 2) + 1j * torch.randn(8, 4, 2)

# Compute the 1D FFT along the last dimension
result = torch.fft.fft(x, dim=-1, norm='ortho')

print(result)