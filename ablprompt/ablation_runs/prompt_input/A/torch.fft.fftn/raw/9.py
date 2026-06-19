import torch

# Create a random tensor
x = torch.randn(4, 4, 4)

# Compute the N-dimensional FFT of x
X = torch.fft.fftn(x)

print(X)