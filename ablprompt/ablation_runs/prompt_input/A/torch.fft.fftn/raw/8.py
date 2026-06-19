import torch

# Create a random tensor
x = torch.randn(2, 3, 4)

# Compute the n-dimensional FFT of the tensor
X = torch.fft.fftn(x)

print(X)