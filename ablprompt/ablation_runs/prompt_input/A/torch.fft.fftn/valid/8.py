import torch

# Create a random tensor
x = torch.randn(4, 5, 6)

# Compute the N-dimensional FFT
X = torch.fft.fftn(x)

print(X)