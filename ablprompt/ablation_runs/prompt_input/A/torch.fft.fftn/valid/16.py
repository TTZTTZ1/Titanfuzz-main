import torch

# Create a random tensor
x = torch.randn(4, 4, 4)

# Compute the N-dimensional FFT
result = torch.fft.fftn(x)

print(result)