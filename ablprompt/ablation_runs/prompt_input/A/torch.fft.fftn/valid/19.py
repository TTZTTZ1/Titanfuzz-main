import torch

# Create a random tensor
x = torch.randn(3, 4, 5)

# Compute the N-dimensional FFT of x
X = torch.fft.fftn(x)

print(X)